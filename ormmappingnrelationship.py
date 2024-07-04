 

#ORM Mapping and Relationships: 

#Learn how to map Python classes to database tables using SQLAlchemy's ORM. 

#Explore different types of relationships such as one-to-one, one-to-many, and many-to-many. 

#Create Python classes for Account, deposits and withdrawals. 

#Create tables in postgres using alembic migrations. 



from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

DATABASE_URL = "postgresql+psycopg2://username:"""

# Create engine and base
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Define models
class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    deposits = relationship('Deposit', back_populates='account')
    withdrawals = relationship('Withdrawal', back_populates='account')

class Deposit(Base):
    __tablename__ = 'deposits'
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    account = relationship('Account', back_populates='deposits')

class Withdrawal(Base):
    __tablename__ = 'withdrawals'
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    account = relationship('Account', back_populates='withdrawals')

# Create tables
Base.metadata.create_all(engine)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()
