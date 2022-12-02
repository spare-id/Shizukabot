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
    ABOUT_BOT_TEXT = """<b>🤖 My Name : <a href=https://t.me/ShizukaMinamotobot><b>Shizuka Minamoto</b></a>\n
👨‍💻 Developer : <a href=https://t.me/aarthur_dayne><b>Arthur Dayne</b></a>\n
🧑‍💻 Co-Developer : <a href=https://t.me/astatine_085><b>Astatine 85</b></a>\n
📝 Language : <a href='https://docs.pyrogram.org/'> Pyrogram</a>\n
📚 Framework : <a href='https://www.python.org'> Python V3</a>\n
📡 Hosted on : <a href='https://www.liquidweb.com'> Liquid Web</a>\n
📢 Updates : <a href=https://t.me/movies_halt_update><b></b>Click Here</a>\n
🌟 Version : <a href='https://www.google.com'> v 1.0</a>\n</b>"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Creator : <a href='https://t.me/aarthur_dayne'>Arthur Dayne</a>
If You Want Your Own Bot Like This Then You Can Contact Our Creator.</b>
"""

    HOME_TEXT = '''<b>Hello {} 👋🏻 Im Shizuka. I am here with unlimited auto filters for you 😁.</b>

<i>Add Me To Your Group To See The Magic Or Read More From The Menu Below</i>'''


    START_MSG = '''<b>Hello {} 👋🏻 Im Shizuka. I am here with unlimited auto filters for you 😁.</b>

<i>Add Me To Your Group To See The Magic Or Read More From The Menu Below</i>'''


