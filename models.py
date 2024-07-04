from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

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
