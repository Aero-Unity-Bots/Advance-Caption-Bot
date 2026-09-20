# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

import threading

from flask import Flask

from bot import Bot


app = Flask(__name__)


# ------------------------ #
# HOME
# ------------------------ #

@app.route("/")
def hello_world():
    return "ᴍᴏʜᴀᴍᴍᴇᴅ ᴅᴇᴠᴇʟᴏᴘᴇʀ"


# ------------------------ #
# START TELEGRAM BOT
# ------------------------ #

def start_bot():

    try:
        print("🚀 Starting Telegram Bot...")

        bot = Bot()
        bot.run()

    except Exception as e:
        print(f"❌ Telegram Bot Error: {e}")


# ------------------------ #
# RUN BOT IN BACKGROUND
# ------------------------ #

bot_thread = threading.Thread(
    target=start_bot,
    daemon=True
)

bot_thread.start()


# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #
