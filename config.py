import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "TG Video player")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "subhan0111")
ALIVE_NAME = getenv("ALIVE_NAME", "subhan")
BOT_USERNAME = getenv("BOT_USERNAME", "video_player_KDbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "vidieoplayer")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Hollywood_0980")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "kd_botz")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/de3dce819a91c99243f9e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/subhan-1/TG-VIDEO-PLAYER")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/bf986b5076c60acd6d951.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/36f1926e871aea03e96c6.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/26339f392fb2e769e5e9d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/ba978e0e28647401a2b35.jpg")
