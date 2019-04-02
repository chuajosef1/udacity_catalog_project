from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

# Create database and create a shortcut for easier to update database
engine = create_engine('sqlite:///catalogs.db')
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

category2 = Categories(name='Armorer', user_id=1)
session.add(category1)
session.commit()

category3 = Categories(name='Blacksmith', user_id=1)
session.add(category1)
session.commit()

category4 = Categories(name='Carpenter', user_id=1)
session.add(category1)
session.commit()

category5 = Categories(name='Culinarian', user_id=1)
session.add(category1)
session.commit()

category6 = Categories(name='Goldsmith', user_id=1)
session.add(category1)
session.commit()

category7 = Categories(name='Leatherworker', user_id=1)
session.add(category1)
session.commit()

category8 = Categories(name='Weaver', user_id=1)
session.add(category1)
session.commit()

print('Items committed')
