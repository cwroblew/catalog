
function init() {
  gapi.load('auth2', function() {
      // Ready.
  });
}
function onSignIn(authResult) {
    if (authResult['code']) {

        // Hide the sign-in button now that the user is authorized, for example:
        $('#signinButton').attr('style', 'display: none');

        // Send the code to the server
        $.ajax({
            type: 'POST',
            url: '/gconnect?state=' + state,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
            processData: false,
            contentType: 'application/octet-stream; charset=utf-8',
            data: authResult['code'],
            success: function (result) {
                if (result) {
                    $('#result').html('Login Successful!<br>' + result + '<br>Redirecting...')
                    setTimeout(function () {
                        window.location.href = "/catalog";
                    }, 4000);
                } else if (authResult['error']) {
                    console.log('There was an error: ' + authResult['error']);
                } else {
                    $('#result').html('Failed to make a server-side call. Check your configuration and console.');
                }

            }
        });
    }
}

function onSignInFailure() {
    // Handle sign-in errors
    console.log('There was an error: ' + authResult['error']);
 }

 var revokeAllScopes = function() {
  auth2.disconnect();
}