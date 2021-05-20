import os
import motor.motor_asyncio

MONGODB_URL='mongodb://127.0.0.1:27017'
# os.getenv("MONGODB_URL")
mongo = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
mail_db = mongo['postal-logistics']
