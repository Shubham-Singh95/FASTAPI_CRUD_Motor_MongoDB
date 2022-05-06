import motor.motor_asyncio

MONGODB_URL = 'mongodb://127.0.0.1:27017/'

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

# connect to database python_db
database = client.python_db

