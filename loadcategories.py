from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Category, Base, Item, User
# import authorization

engine = create_engine("sqlite:///catalog.db")
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won"t be persisted into the database until you call
# session.commit(). If you"re not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# 1. Beverages - coffee, tea, juice, soda
# 2. Bread/Bakery - bread, rolls, tortillas, bagels
# 3. Canned/Jarred - vegetable, spaghetti, mayonaise, Ketchup
# 4. Dairy - cheese, eggs, milk, yogurt, butter
# 5. Dry/Baking Goods - cereal, flour, sugar, pasta, mixes
# 6. Frozen - waffles, vegatables, ice cream, tv dinners
# 7. Meat/Fish - lunch meat, poultry, beef, port, fish
# 8. Produce - fruits, vegetables
# 9. Other - baby, cat, dog

# Create dummy user
User1 = User(name="Charlene Wroblewski", email="cwroblew+catalog@gmail.com",
             picture="https://www.facebook.com/photo.php?fbid=10204105998147240")
session.add(User1)
session.commit()

# add categories and initial items
category1 = Category(name="Beverages", description="coffee, tea, juice, soda")
session.add(category1)
session.commit()

item1 = Item(
    name="Berres Brothers Sumatra",
    description="12 oz. Sumatra Dark Coffee",
    category=category1
)
session.add(item1)
session.commit()

item2 = Item(
    name="Good Earth Organic Herbal Tea Caffeine Free Sweet & Spicy",
    description="Naturally caffeine free rooibos red tea infused with spicy cinnamon and sweet orange",
    category=category1
)
session.add(item2)
session.commit()

category2 = Category(name="Bread/Bakery", description="bread, rolls, tortillas, bagels")
session.add(category2)
session.commit()

item3 = Item(
    name="Pepperidge Farm Whole Grain Bread",
    description="""
    Always crafted with 100% Whole Grain flour, Pepperidge Farm Whole Grain breads are delicious, with a good source of 
    fiber... our way of helping you maintain a balanced, healthy lifestyle.
    """,
    category=category2
)
session.add(item3)
session.commit()

item4 = Item(
    name="David's Deli: Plain Bagels",
    description="David's Deli: Plain Bagels, 5 ct, 14.25 oz",
    category=category2)
session.add(item4)
session.commit()

category3 = Category(name="Canned/Jarred", description="vegetable, spaghetti, mayonaise, Ketchup")
session.add(category3)
session.commit()

item5 = Item(
    name="Libby's Cream Style Sweet Corn",
    description="8.5 Oz. Can Cream Style Sweet Corn",
    category=category3)
session.add(item5)
session.commit()

category4 = Category(name="Dairy", description="cheese, eggs, milk, yogurt, butter")
session.add(category4)
session.commit()

item6 = Item(
    name="Kemps 1% Low Fat Milk (Plastic Gallon)",
    description="Rich, protein and nutrient rich milk with only 1% fat.",
    category=category4)
session.add(item6)
session.commit()

item7 = Item(
    name="Simple Truth Organic Plain Greek Nonfat Yogurt",
    description="32 Oz tub of Plain Greek Nonfat Yogurt",
    category=category4)
session.add(item7)
session.commit()

category5 = Category(name="Dry/Baking Goods", description="cereal, flour, sugar, pasta, mixes")
session.add(category5)
session.commit()

item8 = Item(
    name="bear naked original cinnamon granola",
    description="""
    Non-GMO project verified whole grain oats, honey, dried cranberries, sunflower seeds, and cinnamon make it a nature 
    lover's delight with 6g of protein per serving
    """,
    category=category5)
session.add(item8)
session.commit()

category6 = Category(name="Frozen", description="waffles, vegatables, ice cream, tv dinners")
session.add(category6)
session.commit()

item9 = Item(
    name="FLAV-R-PAC Brussel Sprouts",
    description="Tender sprouts with mild, distinctive flavor",
    category=category6)
session.add(item9)
session.commit()

category7 = Category(name="Meat/Fish", description="lunch meat, poultry, beef, port, fish")
session.add(category7)
session.commit()

item10 = Item(
    name="Kroger Turkey Breast, Honey, Deli Thin Sliced",
    description="16 Oz honey roasted Turkey, deli thin sliced",
    category=category7)
session.add(item10)
session.commit()

category8 = Category(name="Produce", description="fruits, vegetables")
session.add(category8)
session.commit()

item11 = Item(
    name="Ruby Frost Apple",
    description="""
    RubyFrost apples are the perfect balance of sweet and tart, deep and rich with a hearty crunch and ideal crisp 
    texture.
    """,
    category=category8)
session.add(item11)
session.commit()

category9 = Category(name="Other", description="baby, cat, dog")
session.add(category9)
session.commit()

item12 = Item(
    name="Dave's Naturally Healthy Grain Free Canned Cat Food Chicken and Herring Dinner Formula",
    description="""
    Dave's Naturally Healthy Grain Free Canned Cat Food 5.5oz is the best value for a good quality Grain-Free canned cat 
    food you can buy.
    """,
    category=category9)
session.add(item12)
session.commit()
