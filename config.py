## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgAM49rPMe8ELmEJzel1Zynvn2UHhk7gYzJ1WipnCgWlRMAfEDvpHSFRPArtbD6Vma0MsNktX1gnZMGFpdxt_D-nTZF8Z6zlCr4Qx8AeM6v4cvQseHs1JhA4ZcdPh4eb1qVIw4EG8hRB0oFZpm8B4M3Nl5Tw6QVEdi_QnEtm22I77qfGDVucD046G-zT6NemiJKdbN4s9rn9WhMDgtSaNy1ICnxbmybPvjxa7Z1dAc8787rJccCtuQEJ816_ZgLoGfvEaoY1ZIoJvd5FCT5Ju2UvEQkO-tkMps6msPiCJBctCAuwnUeE0lfNJbGMvECgtnAOGY3xMehF5tjU-ft89-viAAAAATAvZtQA")
BOT_TOKEN = getenv("BOT_TOKEN", "5416717850:AAE79VKGyeyLOCe4l1CTinRa9QMpRcHK0Bg")
BOT_NAME = getenv("BOT_NAME", "moscibot")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "S †.")
OWNER_USERNAME = getenv("OWNER_USERNAME", "llll5PP")
ALIVE_NAME = getenv("ALIVE_NAME", "S †.")
BOT_USERNAME = getenv("BOT_USERNAME", "moscibot")
OWNER_ID = getenv("OWNER_ID", "1854384004")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "muscikR")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "lIZllZ")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "llll5PP")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1150979599").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
