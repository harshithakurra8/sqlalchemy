from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Create an engine
engine = create_engine('sqlite:///example.db')

# Create a MetaData object
metadata = MetaData()

# Define a table
users_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('email', String, unique=True)
)

# Create the table in the database
metadata.create_all(engine)

# Reflect existing tables
metadata.reflect(bind=engine)

# Access the reflected table
reflected_users_table = metadata.tables['users']

# List all table names
print(metadata.tables.keys())

# Get column information
for column in reflected_users_table.columns:
    print(column.name, column.type)

# Drop all tables
metadata.drop_all(engine)
