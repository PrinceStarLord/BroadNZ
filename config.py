import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5841213132:AAH3ssZLfkeVjlUyvxyim2970tP2pEYeXF4")
API_ID = int(os.environ.get("API_ID", "5291894"))
API_HASH = os.environ.get("API_HASH", "e15ad5a64cb8bd39b2be463d0314295f")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001668544004"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1132901778").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://renamev3-1:renamev3-1@cluster0.hyv9toa.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot1")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
