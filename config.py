from os import environ

API_ID = int(environ.get("API_ID", "27823209"))
API_HASH = environ.get("API_HASH", "1d693fcf3bfea119ca1d9057b08a4495")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002364462279"))
ADMIN = int(environ.get("ADMIN", "6004928770"))
DB_URI = environ.get("DB_URI", "mongodb+srv://autoacceptbot:autoacceptbot@cluster0.a64dz8p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "Cluster0")
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
IS_FSUB = bool(environ.get("FSUB", True))
AUTH_CHANNELS = environ.get("AUTH_CHANNEL", "-1002327045567")
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")]
