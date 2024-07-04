from sqlalchemy.orm import sessionmaker

from model import User,engine

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a new session
db = SessionLocal()

# Create a new user instance
new_user = User(name="John Doe", email="john@example.com")

# Add the user to the session and commit the transaction
db.add(new_user)
db.commit()

# Query the database for the user
user = db.query(User).filter(User.email == "john@example.com").first()
print(user.name)
