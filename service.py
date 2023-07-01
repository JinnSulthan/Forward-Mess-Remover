import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot_token = os.environ.get("BOT_TOKEN")
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

app = Client(
    "Forward-Mess-Remover",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash
)

START_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('SOURCE CODE', url="https://github.com/SpamShield/Forward-Mess-Remover")
        ]
    ]
)

@app.on_message(filters.private & filters.command("start"))
async def start(_, message):
    await message.reply_sticker("CAACAgUAAxkBAAEBcr1hsLH3Nu0-qQpwwWQ7FkF58xnwSgACpAMAAjieoFU-Q-udLfwBUx4E")
    await message.reply_text(
        f"Hai {message.from_user.mention}, I am Forward-Mess-Remover Bot.",
        disable_web_page_preview=True,
        reply_markup=START_BUTTON
    )

@app.on_message(filters.forwarded)
async def delete(_, message):
    await message.delete()

app.run()
