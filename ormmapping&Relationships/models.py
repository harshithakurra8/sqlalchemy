#1.	ORM Mapping and Relationships:
#o	Learn how to map Python classes to database tables using SQLAlchemy's ORM.
#o	Explore different types of relationships such as one-to-one, one-to-many, and many-to-many.
#o	Create Python classes for Account, deposits and withdrawals.
#o	Create tables in postgres using alembic migrations.





from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    balance = Column(Float, default=0.0)
    deposits = relationship("Deposit", back_populates="account")
    withdrawals = relationship("Withdrawal", back_populates="account")

class Deposit(Base):
    __tablename__ = 'deposits'
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    account = relationship("Account", back_populates="deposits")

class Withdrawal(Base):
    __tablename__ = 'withdrawals'
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    account = relationship("Account", back_populates="withdrawals")
