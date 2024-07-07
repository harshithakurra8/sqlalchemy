#2.	Querying and Filtering Data:
#o	Understand how to use SQLAlchemy's query API to fetch and filter data from the database.
#o	Learn about filtering, sorting, and aggregating data using SQLAlchemy's query expressions.
#o	Query transactions based on account type, balance available, transactions etc.
#o	Implement sorting and pagination for transaction listings.







from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import and_, or_

Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    account_type = Column(String)
    balance = Column(Float)
    transactions = relationship("Transaction", back_populates="account")

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    amount = Column(Float)
    description = Column(String)
    account = relationship("Account", back_populates="transactions")

engine = create_engine('sqlite:///bank.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Query transactions for 'Savings' accounts with balance > 1000, sorted by amount, paginated
page = 1
page_size = 10

transactions = session.query(Transaction).join(Account).filter(
    and_(Account.account_type == 'Savings', Account.balance > 1000)
).order_by(Transaction.amount.desc()).limit(page_size).offset((page - 1) * page_size).all()

for transaction in transactions:
    print(transaction.id, transaction.amount, transaction.description)



