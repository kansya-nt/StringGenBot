from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("20609170"))
API_HASH = getenv("cd0fa6d4f7c452ec5617bb0b1e4dc479")

BOT_TOKEN = getenv("6742240257:AAHH7RDQILs6eHQFtdXwy02eLFsuNheQsx0")
MONGO_DB_URI = getenv("mongodb+srv://babunt1:1234@cluster0.8wb8vhj.mongodb.net/?retryWrites=true&w=majority", None)

OWNER_ID = int(getenv("OWNER_ID", 1499130346))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Asupanhot_viral")
