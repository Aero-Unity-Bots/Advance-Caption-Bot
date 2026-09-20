

import threading
import traceback

from flask import Flask

from bot import Bot

app = Flask(name)

@app.route("/")
def hello_world():
return "ᴍᴏʜᴀᴍᴍᴇᴅ ᴅᴇᴠᴇʟᴏᴘᴇʀ"

def start_bot():

try:
    print("🚀 Starting Telegram Bot...")

    bot = Bot()

    print("🔌 Telegram Bot Instance Created")

    bot.run()

except Exception as e:
    print(f"❌ Telegram Bot Error: {e}")
    traceback.print_exc()

bot_thread = threading.Thread(
target=start_bot,
daemon=True,
name="TelegramBotThread"
)

bot_thread.start()

