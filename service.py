import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, User, Message

Client = Client(
    "Forward-Mess-Remover",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('SOURCE CODE', url="https://github.com/SpamShield/Forward-Mess-Remover")
        ]]
    ) 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, message):
    await message.reply_sticker("CAACAgUAAxkBAAEBcr1hsLH3Nu0-qQpwwWQ7FkF58xnwSgACpAMAAjieoFU-Q-udLfwBUx4E")
    await message.reply_text(
        f""" Hai {message.from_user.mention} am Forward-Mess-Remover Bot.""", 
        disable_web_page_preview=True,
        reply_markup=START_BUTTON
    )
@Client.on_message(filters.forwarded)
async def delete(bot,message):
 await message.delete()

Client.run()
