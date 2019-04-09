from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

# Create database and create a shortcut for easier to update database
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create Test User
User1 = User(name='Test User', email='jchua2012@gmail.com')
session.add(User1)
session.commit()

category1 = Categories(name='Alchemist', user_id=1)
session.add(category1)
session.commit()

categoryItem1 = CategoryItem(
    name='Quicksilver',
    description='Liquid metal widely utilized by alchemists in\
    the production of firesand and by\
    smiths in the production of alloys. ',
    user_id=1,
    category=category1)
session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(
    name='Potion of Vitality',
    description='This weak concoction temporarily increases vitality.',
    user_id=1,
    category=category1)
session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(
    name='Lanolin',
    description='A waxy yellow substance extracted from sheep\
    wool and used in ointments as well as to prevent rusting.',
    user_id=1,
    category=category1)
session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(
    name='Max-Potion',
    description='This spiritous concoction instantly\
    restores a considerable amount of HP.',
    user_id=1,
    category=category1)
session.add(categoryItem4)
session.commit()

categoryItem5 = CategoryItem(
    name='Super-Ether',
    description='Processed via the alchemical extraction of\
    aetheric essence occurring in elemental crystals,\
    the contents of this vial instantly restore a significant amount of MP.',
    user_id=1,
    category=category1)
session.add(categoryItem5)
session.commit()

category2 = Categories(name='Armorer', user_id=1)
session.add(category2)
session.commit()

categoryItem6 = CategoryItem(
    name='Bronze Ingot',
    description='An ingot of smelted bronze.',
    user_id=1,
    category=category2)
session.add(categoryItem6)
session.commit()

categoryItem7 = CategoryItem(
    name='Iron Cuirass',
    description='A piece of iron armor consisting of breastplate\
    and backplate fastened together.',
    user_id=1,
    category=category2)
session.add(categoryItem7)
session.commit()

categoryItem8 = CategoryItem(
    name='Mythril Plate',
    description='A sheet of hammered mythril.',
    user_id=1,
    category=category2)
session.add(categoryItem8)
session.commit()

categoryItem9 = CategoryItem(
    name='Titanium Hoplon',
    description='A heavy titanium shield.',
    user_id=1,
    category=category2)
session.add(categoryItem9)
session.commit()

categoryItem10 = CategoryItem(
    name='Molybdenum Ingot',
    description='An ingot of smelted molybdenum.',
    user_id=1,
    category=category2)
session.add(categoryItem10)
session.commit()

category3 = Categories(name='Blacksmith', user_id=1)
session.add(category3)
session.commit()

categoryItem11 = CategoryItem(
    name='Bronze Rivets',
    description='Short bronze pins with large heads. \
    Used in connecting metal plates.',
    user_id=1,
    category=category3)
session.add(categoryItem11)
session.commit()

categoryItem12 = CategoryItem(
    name='Iron Daggers',
    description='A pair of daggers forged with iron ore.',
    user_id=1,
    category=category3)
session.add(categoryItem12)
session.commit()

categoryItem13 = CategoryItem(
    name='Mythril Rivets',
    description='Short mythril pins with large heads. \
    Used in connecting metal plates. ',
    user_id=1,
    category=category3)
session.add(categoryItem13)
session.commit()

categoryItem14 = CategoryItem(
    name='Cobalt Claws',
    description='A pair of metal claws forged with cobalt ore',
    user_id=1,
    category=category3)
session.add(categoryItem14)
session.commit()

categoryItem15 = CategoryItem(
    name='Oroshigane Ingot',
    description='An ingot of Doman iron, smelted using Far Eastern techniques.',
    user_id=1,
    category=category3)
session.add(categoryItem15)
session.commit()

category4 = Categories(name='Carpenter', user_id=1)
session.add(category4)
session.commit()

categoryItem16 = CategoryItem(
    name='Maple Lumber',
    description='Processed maple logs.',
    user_id=1,
    category=category4)
session.add(categoryItem16)
session.commit()

categoryItem17 = CategoryItem(
    name='Elm Longbow',
    description='A type of bow crafted using Elm wood as its base.',
    user_id=1,
    category=category4)
session.add(categoryItem17)
session.commit()

categoryItem18 = CategoryItem(
    name='Mahogany Lumber',
    description='Processed mahogany logs',
    user_id=1,
    category=category4)
session.add(categoryItem18)
session.commit()

categoryItem19 = CategoryItem(
    name='Birch Longbow',
    description='A type of bow crafted using Birch wood as its base.',
    user_id=1,
    category=category4)
session.add(categoryItem19)
session.commit()

categoryItem20 = CategoryItem(
    name='Zelkov Lumber',
    description='Processed zelkov logs',
    user_id=1,
    category=category4)
session.add(categoryItem20)
session.commit()

category5 = Categories(name='Culinarian', user_id=1)
session.add(category5)
session.commit()

categoryItem21 = CategoryItem(
    name='Table Salt',
    description='Finely ground salt used not only for \
    flavoring foods, but for pickling and preserving as well.',
    user_id=1,
    category=category5)
session.add(categoryItem21)
session.commit()

categoryItem22 = CategoryItem(
    name='Walnut Bread',
    description='A soft white bread filled with fragrant walnuts.',
    user_id=1,
    category=category5)
session.add(categoryItem22)
session.commit()

categoryItem23 = CategoryItem(
    name='Ratatouille',
    description='A nutritious soup made from a variety \
    of vegetables sauteed in lavender oil.',
    user_id=1,
    category=category5)
session.add(categoryItem23)
session.commit()

categoryItem24 = CategoryItem(
    name='Vermicelli',
    description='Thin noodles made with highland flour, \
    eggs, water, and salt. These have been dried \
    and will keep indefinitely.',
    user_id=1,
    category=category5)
session.add(categoryItem24)
session.commit()

categoryItem25 = CategoryItem(
    name='Chirashi-zushi',
    description='A Hingan dish sushi,this iteration consists of\
    a full bowl of sweet vinegared rice \
    topped with various items such as thinly sliced omelet, salted \
    fish eggs, dried gourd, stewed mushrooms, and other local fare.',
    user_id=1,
    category=category5)
session.add(categoryItem25)
session.commit()

category6 = Categories(name='Goldsmith', user_id=1)
session.add(category6)
session.commit()

categoryItem26 = CategoryItem(
    name='Copper Gorget',
    description='An article of clothing that covers the throat made of copper.',
    user_id=1,
    category=category6)
session.add(categoryItem26)
session.commit()

categoryItem27 = CategoryItem(
    name='Brass Earrings',
    description='A pair of finely made earrings crafted using brass.',
    user_id=1,
    category=category6)
session.add(categoryItem27)
session.commit()

categoryItem28 = CategoryItem(
    name='Jadeite',
    description='A hard piece of jade.',
    user_id=1,
    category=category6)
session.add(categoryItem28)
session.commit()

categoryItem29 = CategoryItem(
    name='Chrysolite',
    description='A green jewel.',
    user_id=1,
    category=category6)
session.add(categoryItem29)
session.commit()

categoryItem30 = CategoryItem(
    name='Rhodonite',
    description='A blood red jewel.',
    user_id=1,
    category=category6)
session.add(categoryItem30)
session.commit()

category7 = Categories(name='Leatherworker', user_id=1)
session.add(category7)
session.commit()

categoryItem31 = CategoryItem(
    name='Leather',
    description='A large piece of cured animal skin.',
    user_id=1,
    category=category7)
session.add(categoryItem31)
session.commit()

categoryItem32 = CategoryItem(
    name='Goatskin Leggings',
    description='A pair of leggings made from Goatskin',
    user_id=1,
    category=category7)
session.add(categoryItem32)
session.commit()

categoryItem33 = CategoryItem(
    name='Peiste Leather',
    description='A large piece of cured peiste skin.',
    user_id=1,
    category=category7)
session.add(categoryItem33)
session.commit()

categoryItem34 = CategoryItem(
    name='Dragonskin Boots',
    description='A pair of boots made from Dragonskin',
    user_id=1,
    category=category7)
session.add(categoryItem34)
session.commit()

categoryItem35 = CategoryItem(
    name='Gazelle Leather',
    description='A large piece of cured gazelle hide.',
    user_id=1,
    category=category7)
session.add(categoryItem35)
session.commit()

category8 = Categories(name='Weaver', user_id=1)
session.add(category8)
session.commit()

categoryItem36 = CategoryItem(
    name='Hempen Yarn',
    description='Coarse yarn spun from moko grass fiber.',
    user_id=1,
    category=category8)
session.add(categoryItem36)
session.commit()

categoryItem37 = CategoryItem(
    name='Cotton Coif',
    description='A head piece weaved with the finest cotton.',
    user_id=1,
    category=category8)
session.add(categoryItem37)
session.commit()

categoryItem38 = CategoryItem(
    name='Woolen Yarn',
    description='Heavy yarn spun from sheep fleece.',
    user_id=1,
    category=category8)
session.add(categoryItem38)
session.commit()

categoryItem39 = CategoryItem(
    name='Ramie Skirt',
    description='A skirt made from ramie',
    user_id=1,
    category=category8)
session.add(categoryItem39)
session.commit()

categoryItem40 = CategoryItem(
    name='Winter Sweater',
    description='A sweater that can keep you warm during the winter season.',
    user_id=1,
    category=category8)
session.add(categoryItem40)
session.commit()

print('Items committed')
