from pymongo import MongoClient
import ssl
from core import config
# ssl._create_default_https_context = ssl._create_unverified_context
# , ssl=True, ssl_cert_reqs=ssl.CERT_NONE

client = MongoClient("mongodb+srv://"+config.settings.user_name+":"+config.settings.pass_word+"@"+config.settings.host+"/myFirstDatabase?retryWrites=true&w=majority")

db = client.todo_app

collection_name = db["todos_app"]
students_collection = db["students"]
courses_collection = db["courses"]
