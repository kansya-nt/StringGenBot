from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv(""))
API_HASH = getenv("")

BOT_TOKEN = getenv("")
MONGO_DB_URI = getenv("")
OWNER_ID = int(getenv("OWNER_ID", 1499130346))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Asupanhot_viral")
