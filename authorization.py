from flask import request, make_response, flash
from flask import session as login_session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

import httplib2

import json

import requests

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


class Authorization:
    def __init__(self):
        print("initialized")

    @staticmethod
    def gconnect():
        # Validate state token
        if not request.headers.get('X-Requested-With'):
            abort(403)

        state = login_session['state']
        if request.args.get('state') != state:
            response = make_response(json.dumps('Invalid state parameter.'), 401)
            response.headers['Content-Type'] = 'application/json'
            return response
        # Obtain authorization code
        code = request.data
        print(code)
        # authorization_response = request.url

        try:
            oauth_flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
                'client_secrets.json',
                scopes=None,
                state=state
            )
            oauth_flow.redirect_uri = 'postmessage'
            oauth_flow.fetch_token(code=code)

            # Store the credentials in the session.
            # ACTION ITEM for developers:
            #     Store user's access and refresh tokens in your data store if
            #     incorporating this code into your real app.
            credentials = oauth_flow.credentials
            login_session['credentials'] = {
                'token': credentials.token,
                'refresh_token': credentials.refresh_token,
                'token_uri': credentials.token_uri,
                'client_id': credentials.client_id,
                'client_secret': credentials.client_secret,
                'scopes': credentials.scopes}
        except ValueError:
            response = make_response(
                json.dumps('Failed to upgrade the authorization code.'), 401)
            response.headers['Content-Type'] = 'application/json'
            return response

        # Check that the access token is valid.
        access_token = credentials.token
        url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
               % access_token)
        h = httplib2.Http()
        result = json.loads(h.request(url, 'GET')[1])

        # If there was an error in the access token info, abort.
        if result.get('error') is not None:
            response = make_response(json.dumps(result.get('error')), 500)
            response.headers['Content-Type'] = 'application/json'
            return response

        # gplus_id = credentials.id_token['sub']
        # if result['user_id'] != gplus_id:
        #     response = make_response(
        #         json.dumps("Token's user ID doesn't match given user ID."), 401)
        #     response.headers['Content-Type'] = 'application/json'
        #     return response

        stored_access_token = login_session.get('access_token')

        # stored_gplus_id = login_session.get('gplus_id')
        if stored_access_token is not None:  # and gplus_id == stored_gplus_id:
            print("Stored access token is not None")
            response = make_response(json.dumps('Current user is already connected.'),
                                     200)
            response.headers['Content-Type'] = 'application/json'
            return response

        # Store the access token in the session for later use.
        login_session['access_token'] = credentials.token
        # login_session['gplus_id'] = gplus_id

        # Get user info
        userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
        params = {'access_token': credentials.token, 'alt': 'json'}
        answer = requests.get(userinfo_url, params=params)

        data = answer.json()
        print(data)

        login_session['provider'] = 'google'
        login_session['username'] = data['name']
        login_session['picture'] = data['picture']
        login_session['email'] = data['email']

        # see if user exists, if it doesn't make a new one
        user_id = getUserID(data["email"])
        if not user_id:
            user_id = createUser(login_session)
        login_session['user_id'] = user_id
        print("User")
        print(user_id)

        output = ''
        output += '<h1>Welcome, '
        output += login_session['username']
        output += '!</h1>'
        output += '<img src="'
        output += login_session['picture']
        output += \
            ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
        flash("you are now logged in as %s" % login_session['username'])
        print("done!")
        return output

    # User Helper Functions
    @staticmethod
    def createUser(login_session):
        newUser = User(name=login_session['username'], email=login_session[
                       'email'], picture=login_session['picture'])
        session.add(newUser)
        session.commit()
        user = session.query(User).filter_by(email=login_session['email']).one()
        return user.id

    @staticmethod
    def getUserInfo(user_id):
        user = session.query(User).filter_by(id=user_id).one()
        return user

    @staticmethod
    def getUserID(email):
        try:
            user = session.query(User).filter_by(email=email).one()
            print("User id = % " % user.id)
            return user.id
        except:
            print("Error with user id")
            return None

    @staticmethod
    def is_logged_in():
        if 'username' not in login_session:
            return True
        else:
            return False

    @staticmethod
    def disconnect():


    def fbdisconnect(self):
        facebook_id = login_session['facebook_id']
        # The access token must me included to successfully logout
        access_token = login_session['access_token']
        url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id,access_token)
        h = httplib2.Http()
        result = h.request(url, 'DELETE')[1]
        return "you have been logged out"

    def gdisconnect(self):
        # Only disconnect a connected user.
        access_token = login_session.get('access_token')
        print(access_token)
        if access_token is None:
            response = make_response(
                json.dumps('Current user not connected.'), 401)
            response.headers['Content-Type'] = 'application/json'
            return response
        url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
        h = httplib2.Http()
        result = h.request(url, 'GET')[0]
        print(result)

        if result['status'] == '200':
            # Reset the user's sesson.
            del login_session['access_token']
            #del login_session['gplus_id']
            print (login_session)

            response = make_response(json.dumps('Successfully disconnected.'), 200)
            response.headers['Content-Type'] = 'application/json'
            return response
        else:
            # For whatever reason, the given token was invalid.
            response = make_response(
                json.dumps('Failed to revoke token for given user.', 400))
            response.headers['Content-Type'] = 'application/json'
            return response

    @staticmethod
    def getUserID(email):
        try:
            user = session.query(User).filter_by(email=email).one()
            return user.id
        except:
            return None
