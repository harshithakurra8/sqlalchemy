# main.py
from database import SessionLocal
from models import Account, Deposit

session = SessionLocal()

# Create a new account
new_account = Account(name="John Doe")
session.add(new_account)
session.commit()

# Make a deposit
deposit = Deposit(amount=100.0, account_id=new_account.id)
session.add(deposit)
new_account.balance += deposit.amount
session.commit()

# Query the account
account = session.query(Account).filter_by(name="John Doe").first()
print(f"Account: {account.name}, Balance: {account.balance}")


