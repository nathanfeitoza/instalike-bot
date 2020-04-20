from dotenv import load_dotenv
from pathlib import Path
import os
from BotCore import BotCore

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

bot = BotCore()

bot.setLoginInstagram(os.getenv("INSTAGRAM_LOGIN"), os.getenv("INSTAGRAM_PASS"))
bot.setLoginInstalike(os.getenv("INSTALIKE_EMAIL"), os.getenv("INSTALIKE_PASS"))
bot.initBot()