import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MovieSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
🤖 My Name: <a href='http://t.me/ShizukaMinamotobot'>Shizuka Minamoto</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='koyeb.com'>Koyeb</a>

👨‍💻 Created By: <a href='https://t.me/aarthur_dayne'>Arthur Dayne</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Creator : <a href='https://t.me/aarthur_dayne'>Arthur Dayne</a>
If You Want Your Own Bot Like This Then You Can Contact Our Creator.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Shizuka Minamoto.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @movies_halt</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Shizuka Minamoto.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @movies_halt</a></b>
"""

