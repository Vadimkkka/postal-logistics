import os
import motor.motor_asyncio

mongo = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL"))
mail_db = mongo['postal-logistics']
