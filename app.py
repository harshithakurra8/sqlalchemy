from sqlalchemy.orm import sessionmaker

from models import user,engine

Session=sessionmaker(bind=engine)
session=Session()
user=User(name="Harry",age=30)

session.add(user)

session.commit()