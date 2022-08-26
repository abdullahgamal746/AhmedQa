from YukkiMusic.utils.database import is_music_playing, music_off
from strings import get_command
import asyncio
from strings.filters import command
from YukkiMusic import app
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.database import set_loop
from YukkiMusic.utils.decorators import AdminRightsCheck
from YukkiMusic.utils.database import is_muted, mute_on
from YukkiMusic.utils.database import is_muted, mute_off
from YukkiMusic.utils.database import is_music_playing, music_on
from datetime import datetime
from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL, lyrical, START_IMG_URL, MONGO_DB_URI, OWNER_ID
from YukkiMusic.utils import bot_sys_stats
from YukkiMusic.utils.decorators.language import language
import random
import config
import re
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from pyrogram import Client, filters
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
import sys
from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

START_IMG_URL = getenv("START_IMG_URL")

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")
PAUSE_COMMAND = get_command("PAUSE_COMMAND")
MUTE_COMMAND = get_command("MUTE_COMMAND")
UNMUTE_COMMAND = get_command("UNMUTE_COMMAND")
RESUME_COMMAND = get_command("RESUME_COMMAND")
PING_COMMAND = get_command("PING_COMMAND")
LYRICS_COMMAND = get_command("LYRICS_COMMAND")

api_key = "Vd9FvPMOKWfsKJNG9RbZnItaTNIRFzVyyXFdrGHONVsGqHcHBoj3AI3sIlNuqzuf0ZNG8uLcF9wAd5DXBBnUzA"
y = lg.Genius(
    api_key,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True,
)
y.verbose = False


@app.on_message(
    filters.command(["id"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""أسمك {message.from_user.mention}\n\nمعرفك @{message.from_user.username}\n\nآيديك {message.from_user.id}\n\nآيدي الكروب {message.chat.id}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑺𝒐𝒖𝒓𝒄𝒆", url=f"https://t.me/UU_u_3"),
                ],
            ]
        ),
    )

@app.on_message(
    command(["ايدي","الايدي"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""نـيـمـك{message.from_user.mention}\n\nيـوزرك @{message.from_user.username}\n\nالايدي {message.from_user.id}\n\nايـدي الـجـروب{message.chat.id}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑺𝒐𝒖𝒓𝒄𝒆", url=f"https://t.me/UU_u_3"),
                ],
            ]
        ),
    )
    
@app.on_message(
    command(["قول"])
    & filters.group
    & ~filters.edited
)
def echo(client, msg):
    text = msg.text.split(None, 1)[1]
    msg.reply(text)

@app.on_message(
    command(["انا مين"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""انت روحي""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑺𝒐𝒖𝒓𝒄𝒆", url=f"https://t.me/UU_u_3"),
                ],
            ]
        ),
    )
                    
@app.on_message(
     command(["مبرمج السورس","المطور","مطور السورس","المبرمج"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b1969dcd2a460c72daa3b.jpg",
        caption=f"""𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 𝑩𝒐𝒕""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 𝑩𝒐𝒕", url=f"https://t.me/DAD_HiTIER_ALKABiR"),
                ],[
                InlineKeyboardButton(
                        "𝑺𝒐𝒖𝒓𝒄𝒆", url=f"https://t.me/UU_u_3"),
                ]
            ]
        ),
    )

@app.on_message(
    command(["سورس","السورس"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b1969dcd2a460c72daa3b.jpg",
        caption=f"""[𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 𝑩𝒐𝒕](https://t.me/DAD_HiTIER_ALKABiR)""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                        "𝑺𝒐𝒖𝒓𝒄𝒆", url=f"https://t.me/UU_u_3"),
            ],[
                InlineKeyboardButton("✚ أضفني الى مجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
        ]
         ),
     )
  
