from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Store, Base, InventoryItem, User, Category

engine = create_engine('sqlite:///store.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Charlene Wroblewski", email="cwroblew+catalog@gmail.com",
             picture="https://www.facebook.com/photo.php?fbid=10204105998147240")
session.add(User1)
session.commit()

# Catalog for Charlene's Store
store = Store(id=1, name="Charlene's Store")

session.add(store)
session.commit()

category1 = Category(name="Category 1", description="Category 1's description")

session.add(category1)
session.commit()

invItem1 = InventoryItem(user_id=1, name="Inv 1", description="Inventory Item 1", price="$100.00", category_id=1, store_id=1)

session.add(invItem1)
session.commit()

category1 = Category(name="Category 1", description="Category 1's description")

session.add(category1)
session.commit()

invItem1 = InventoryItem(user_id=1, name="Inv 1", description="Inventory Item 1", price="$100.00", category_id=1, store_id=1)

session.add(invItem1)
session.commit()
category1 = Category(name="Category 1", description="Category 1's description")

session.add(category1)
session.commit()

invItem1 = InventoryItem(user_id=1, name="Inv 1", description="Inventory Item 1", price="$100.00", category_id=1, store_id=1)

session.add(invItem1)
session.commit()
category1 = Category(name="Category 1", description="Category 1's description")

session.add(category1)
session.commit()

invItem1 = InventoryItem(user_id=1, name="Inv 1", description="Inventory Item 1", price="$100.00", category_id=1, store_id=1)

session.add(invItem1)
session.commit()
category1 = Category(name="Category 1", description="Category 1's description")

session.add(category1)
session.commit()

invItem1 = InventoryItem(user_id=1, name="Inv 1", description="Inventory Item 1", price="$100.00", category_id=1, store_id=1)

session.add(invItem1)
session.commit()
category1 = Category(name="Category 1", description="Category 1's description")

session.add(category1)
session.commit()

invItem1 = InventoryItem(user_id=1, name="Inv 1", description="Inventory Item 1", price="$100.00", category_id=1, store_id=1)

session.add(invItem1)
session.commit()
category1 = Category(name="Category 1", description="Category 1's description")

session.add(category1)
session.commit()

invItem1 = InventoryItem(user_id=1, name="Inv 1", description="Inventory Item 1", price="$100.00", category_id=1, store_id=1)

session.add(invItem1)
session.commit()
category1 = Category(name="Category 1", description="Category 1's description")

session.add(category1)
session.commit()

invItem1 = InventoryItem(user_id=1, name="Inv 1", description="Inventory Item 1", price="$100.00", category_id=1, store_id=1)

session.add(invItem1)
session.commit()
