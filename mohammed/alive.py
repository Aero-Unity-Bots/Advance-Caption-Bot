# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

import time

from pyrogram import Client, filters
from info import ADMIN


# Put your Telegram sticker file_id here
ALIVE_STICKER = "CgACAgQAAxkBAAIOpmqwBoY0C00jo6t2rIxYpUICEqeTAAItCgACvoykUDAPxxyDdh_CHgQ"


# ------------------------ #
# ALIVE COMMAND
# ADMIN ONLY
# ------------------------ #

@Client.on_message(
    filters.private &
    filters.command("alive")
)
async def alive_command(client, message):

    start_time = time.perf_counter()

    # Send sticker
    await message.reply_sticker(
        sticker=ALIVE_STICKER
    )

    # Calculate ping
    ping = round(
        (time.perf_counter() - start_time) * 1000,
        2
    )

    # Send alive text
    await message.reply_text(
        "<b>╭━━━━━━━━━━━━━━━━━━╮\n"
        "      🤖 Bᴏᴛ Is Aʟɪᴠᴇ!\n"
        "╰━━━━━━━━━━━━━━━━━━╯</b>\n\n"
        f"⚡ <b>Pɪɴɢ:</b> <code>{ping} ms</code>\n"
        "🟢 <b>Sᴛᴀᴛᴜs:</b> Oɴʟɪɴᴇ\n"
        "🚀 <b>Sᴇʀᴠᴇʀ:</b> Rᴜɴɴɪɴɢ\n\n"
        " <b>Yᴏᴜ ᴀʀᴇ ᴠᴇʀʏ ʟᴜᴄᴋʏ 🤞 I ᴀᴍ ᴀʟɪᴠᴇ ❤️ "
        "Pʀᴇss /start ᴛᴏ ᴜsᴇ ᴍᴇ</b>"
    )


# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #
