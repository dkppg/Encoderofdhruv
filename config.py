import os
import dotenv
#import SmartEncoder.Database.db.myDB as db


dotenv.load_dotenv()

class Config(object):
  API_ID = int(os.environ.get("API_ID", 12345))
  API_HASH = os.environ.get("API_HASH")
  BOT_TOKEN = os.environ.get("BOT_TOKEN")
  AUTH_USERS = os.environ.get("AUTH_USERS")
  GOD = os.environ.get("GOD")
  REDIS_HOST = os.environ.get("REDIS_HOST")
 # REDIS_PORT = int(os.environ.get("REDIS_PORT", 12345))
  REDIS_PASS = os.environ.get("REDIS_PASS")
  DOWNLOAD_LOCATION = "downloads"

Config.AUTH_USERS = [1943966786, 5126929234, -1001737980489, 1221558981]
Config.API_ID = 17567723
Config.API_HASH = "b929b76526a9964818f1ed2bd0166d5b"
Config.BOT_TOKEN = "5151739606:AAFMTWQS7mhmvnQVn1bLwgX3s7nY_wf62k8"
Config.REDIS_HOST = "redis-17161.c270.us-east-1-3.ec2.cloud.redislabs.com"
Config.REDIS_PASS = "wIW3pfcwu2UXkkNzsOpRsuX4OomCcexE"
REDIS_PORT = "17161"
