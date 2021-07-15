import asyncio
import sys

from motor import motor_asyncio
from odmantic import AIOEngine
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from Autumn import log
from Autumn.config import get_int_key, get_str_key

MONGO_URI = get_str_key("MONGO_URI")
MONGO_PORT = get_int_key("MONGO_PORT")
MONGO_DB = get_str_key("MONGO_DB")

# Init MongoDB
mongodb = MongoClient(MONGO_URI, MONGO_PORT)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_URI, MONGO_PORT)
db = motor[MONGO_DB]
