import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.environ.get("API_ID", "24547877"))
API_HASH = os.environ.get("API_HASH", "a08a52b2ac7a2afaa5ed0ff089fde9b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

app = Client("newflixpro", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    btn = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Updates", url="https://t.me/newflixpro")],
        [InlineKeyboardButton("➕ Add Me To Group", url="https://t.me/newflixpro_bot?startgroup=true")]
    ])
    await message.reply_text(
        f"**Hello {message.from_user.mention} 👋\n\nI am NewFlixPro Auto-Filter Bot!\n\nJust Add Me To Your Group & Channel!**",
        reply_markup=btn
    )

@app.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_text("**Send any file and I will store it!\nUse /start to begin.**")

print("Bot Started!")
app.run()
