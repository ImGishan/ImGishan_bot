import traceback
import logging
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.types import User, Message
import os
import requests
import time
from pyrogram.errors import UserNotParticipant
import wget
import time
import math
import json
import string
import random
import traceback
import asyncio
import datetime
import aiofiles
from random import choice 
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, InputTextMessageContent
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, UserNotParticipant, UserBannedInChannel
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
from telegraph import upload_file
from youtube_search import YoutubeSearch
import requests
from pytube import YouTube
import youtube_dl
#IMPORT
import traceback
import logging
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.types import User, Message
import os
import requests
import time

from io import BytesIO
from traceback import format_exc
import aiohttp

from pyrogram import Client, filters
from pyrogram.types import Message
from Python_ARQ import ARQ
from pyrogram.types import User, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
import aiohttp
import yt_dlp
from urllib.parse import urlparse
from opencc import OpenCC
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from edit.edit_1 import (  # pylint:disable=import-error
    black_white,
    box_blur,
    bright,
    g_blur,
    mix,
    normal_blur,
)
from edit.edit_2 import (  # pylint:disable=import-error
    cartoon,
    circle_with_bg,
    circle_without_bg,
    contrast,
    edge_curved,
    pencil,
    sepia_mode,
    sticker,
)
from edit.edit_3 import (  # pylint:disable=import-error
    black_border,
    blue_border,
    green_border,
    red_border,
)
from edit.edit_4 import (  # pylint:disable=import-error
    inverted,
    removebg_plain,
    removebg_sticker,
    removebg_white,
    rotate_90,
    rotate_180,
    rotate_270,
    round_sticker,
)
from edit.edit_5 import (  # pylint:disable=import-error
    normalglitch_1,
    normalglitch_2,
    normalglitch_3,
    normalglitch_4,
    normalglitch_5,
    scanlineglitch_1,
    scanlineglitch_2,
    scanlineglitch_3,
    scanlineglitch_4,
    scanlineglitch_5,
)



Client = Client(
    "Test Bot",
    bot_token= "5314301510:AAHgI29NMpGR0fN5E-EGYSdrVcYoOO9ZKpE",
    api_id= 8838171,
    api_hash= "0587408d4f7d9301f5295840b0f3b494",
)

force_subchannel = "GishanKrishka1_Cloud"

BROADCAST_AS_COPY = "True"

OWNER = "ImGishan"

START_IMG = "https://telegra.ph/file/490a71ad194e4d6ea95f0.jpg"

FORCESUB_TEXT = "**❌ Access Denied ❌**\n\n🌷You Must Join My Update Channel...🌷\n♻️Join it & Try Again.♻️"

FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton('༒❣️☢️╣IrØή❂mคŇ╠☢️❣️༒', url=f"https://t.me/{force_subchannel}")
                 ],
                 [
                 InlineKeyboardButton('◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』', url=f"https://t.me/{OWNER}")
                 ],
                 [
                 InlineKeyboardButton(text="♻️ Reload ♻️",callback_data="ref")
                 ]]
                  )


START_STRING =f"""
Hi , Welcome to ◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』's Pm Bot.
Use Help Button For More....

 By [◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』](https://t.me/{OWNER})
"""


START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』', url=f"https://t.me/{OWNER}")
                 ],
                 [
                 InlineKeyboardButton(text="🌴 ʜᴇʟᴘ 🌴",callback_data="cmds")
                 ],
                 [
                 InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ ɢʀᴏᴜᴘ ➕", url="https://t.me/imgishan_Bot?startgroup=true")
                 ]]
                  )

HELP_BUTTONS = InlineKeyboardMarkup([[              
                 InlineKeyboardButton(text="🌻 ᴛᴇʟᴇɢʀᴀᴘʜ 🌻",callback_data="tgm")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 ʟᴏɢᴏ 🌻",callback_data="logoc")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 sᴏɴɢ 🌻",callback_data="songg")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 ᴘɪᴄ ᴍᴇ 🌻",callback_data="pichel")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 ǫʀ ɢᴇɴᴇʀᴀᴛᴏʀ 🌻",callback_data="qrg")
                 ],
                 [
                 InlineKeyboardButton(text="🍃 ʙᴀᴄᴋ 🍃",callback_data="bamk")            
                 ]]
                  )

GHELP_BUTTONS = InlineKeyboardMarkup([[              
                 InlineKeyboardButton(text="🌻 ᴛᴇʟᴇɢʀᴀᴘʜ 🌻",callback_data="htgm")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 ʟᴏɢᴏ 🌻",callback_data="hlogoc")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 sᴏɴɢ 🌻",callback_data="songg")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 ᴘɪᴄ ᴍᴇ 🌻",callback_data="pichel")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 ǫʀ ɢᴇɴᴇʀᴀᴛᴏʀ 🌻",callback_data="hqrg")
                 ],
                 [
                 InlineKeyboardButton(text="🍃 ʙᴀᴄᴋ 🍃",callback_data="hbamk")            
                 ]]
                  )

PICMEH_BUTTONS = InlineKeyboardMarkup([[              
                 InlineKeyboardButton(text="🌻 ᴛᴇʟᴇɢʀᴀᴘʜ 🌻",callback_data="ptgm")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 ʟᴏɢᴏ 🌻",callback_data="plogoc")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 sᴏɴɢ 🌻",callback_data="pongg")
                 ],
                 [
                 InlineKeyboardButton(text="🌻 ǫʀ ɢᴇɴᴇʀᴀᴛᴏʀ 🌻",callback_data="pqrg")
                 ],
                 [
                 InlineKeyboardButton(text="🍃 ʙᴀᴄᴋ 🍃",callback_data="picme")            
                 ]]
                  )
HHHELP_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="🍃 ʙᴀᴄᴋ 🍃",callback_data="hhbak")            
                 ]]
                  ) 
PICMEB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="🍃 ʙᴀᴄᴋ 🍃",callback_data="ppbak")            
                 ]]
                  ) 
                 
BOT_USERNAME = "**@ImGishan_Bot**"
PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
PM_MED_ATT = "<b>Message from:</b> {} \n<b>Name:</b> {}"

TELEGRAPH = """
🍄Help for Telegraph Link Gen🍄

Available commands

✘ Send Eny Photo  - create Telegraph link

"""
PIC_HELP = """
🍄Help for Pic Me🍄

Available commands
✘ /picme - Cappture Ur Profrile Pic 
✘ /addchannel {Ur Channel Id} - Send Pic Me post To Channel or group
"""

LOGO_STRING = """
🍄Help for logo make🍄

Available commands
✘ /logo {text} - create simple random logos
✘ /logohq {text} - create simple random HQ logos
✘ /write{text} - create Note
"""
SONG_STRING = """
🍄Help for song download🍄

Available commands
✘ /song {song name} - Download a song simply.
✘ /song {youtube link} - Download song using youtube link
"""

QR_STRING = """🍄Help for QR Generator🍄

Available commands
✘ /qr {text} - Generate Qr simply.
"""

HELP_STRING = """
⚊❮❮❮❮ ｢  Still Wonder How I Work ? 」❯❯❯❯⚊

✘ Commands Available-

/song {song name}
/logo {text}
/logohq {text}
/write {text}
/qr {text}

Add Onother Features Soon
"""

BACK_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="🍃 ʙᴀᴄᴋ 🍃",callback_data="bamk")
                 ]]
                  )

HELPB_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="ʜᴇʟᴘ⁉️",callback_data="hcmds")
                 ]]
                  )


USER_DETAILS = "<b>PM FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"



picmebtns = InlineKeyboardMarkup([[
               InlineKeyboardButton("🌻 ᴘɪᴄ ᴍᴇ 🌻", callback_data="picme")
               ]]

             )
@Client.on_message(filters.sticker & filters.private)
async def help_me(bot, message):
    file_id = "CAADBQADEwUAAmjn4Vez7jrL1Cu2AAEC"
    await bot.send_sticker(message.chat.id, file_id)
    
@Client.on_message(filters.private & filters.command(["start"]))
async def help_me(bot, message):
    USER = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('USER', url=f"https://t.me/{message.from_user.username}")
                 ]]
                  )
    info = await bot.get_users(user_ids=message.from_user.id)
    USER_DETAILS = f"[{message.from_user.mention}](tg://user?id={message.from_user.id}) [`{message.from_user.id}`] Started Ur Bot.\n\n**PM FROM: `{info.first_name}`**\n**LastName: `{info.last_name}`**\n**Scam: `{info.is_scam}`**\n**Restricted: `{info.is_restricted}`**\n**Status:`{info.status}`**\n**Dc Id: `{info.dc_id}`**"
    await bot.send_message(-1001581011760, text=USER_DETAILS, reply_markup=USER)
    if force_subchannel:
        try:
            user = await bot.get_chat_member(force_subchannel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("Yourt Banned")
                return 
        except UserNotParticipant:
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            await message.reply_text(
            text=text,
            reply_markup=reply_markup
            ) 
            return
    file_id = "CAADBQADgAYAAqwG4FecIIpMGTLeWgI"
    await bot.send_sticker(message.chat.id, file_id)
    text = START_STRING
    reply_markup = START_BUTTON 
    text = START_STRING
    reply_markup = START_BUTTON   
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
            
@Client.on_message(filters.command(["help", "help@ImGishan_Bot"]))  
async def tgm(bot, update):
    reply_markup = InlineKeyboardMarkup([[
                   InlineKeyboardButton(text="ʜᴇʟᴘ⁉️",callback_data="hcmds")
                   ]]
                   )
    await update.reply_text(
    text=f"Hi {update.from_user.mention}\n\n**» press the button below to read the explanation and see the list of available commands !**\n\n__⚡️ Powered by ⚡️__[◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』](t.me/imgishan)",
    reply_markup=reply_markup,
    disable_web_page_preview=True
    )  

@Client.on_message(filters.private & filters.photo)
async def tgm(bot, msg):
    if force_subchannel:
        try:
            user = await bot.get_chat_member(force_subchannel, msg.from_user.id)
            if user.status == "kicked out":
                await msg.reply_text("Yourt Banned")
                return 
        except UserNotParticipant:
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            await msg.reply_text(
                text=text,
                reply_markup=reply_markup
            ) 
            return            
    dwn = await msg.reply_text("Downloading to my server...", True)
    img_path = await msg.download()
    await dwn.edit_text("Uploading as telegra.ph link...")
    try:
        url_path = upload_file(img_path)[0]
    except Exception as error:
        await dwn.edit_text(f"Oops something went wrong\n{error}")
        return
    await dwn.edit_text(
        text=f"<b>Link :-</b> <code>https://telegra.ph{url_path}</code>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Open Link", url=f"https://telegra.ph{url_path}"
                    ),
                    InlineKeyboardButton(
                        text="Share Link",
                        url=f"https://telegram.me/share/url?url=https%3A%2F%2Ftelegra.ph{url_path}%0A%0ALink%20Generate%20by%20%3A%20%40T1V1Bot",
                    )
                ]
            ]
        )
    )
    os.remove(img_path)
    if msg.from_user.id == 1884885842:
        await replay_media(bot, msg)
        return
    info = await bot.get_users(user_ids=msg.from_user.id)
    reference_id = int(msg.chat.id)
    await bot.copy_message(
        chat_id=1884885842,
        from_chat_id=msg.chat.id,
        message_id=msg.message_id,
        caption=PM_MED_ATT.format(reference_id, info.first_name),
        parse_mode="html"
    )
 
@Client.on_message(filters.command("logo"))
async def on_off_antiarab(_, message: Message):
    m = await message.reply_text("**♻ Creating your Logo ♻**......\n\n[░░░░░░░░░░] 00%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇░░░░░░░░] 20%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇░░░░░░] 40%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇░░░░░] 50%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇▇▇░░░] 70%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇▇▇▇░░] 80%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇▇▇▇▇▇] 100%")
    await m.edit("📤Uploading....")
    await m.edit("📤Uploading.....")
    f= message.text
    s=f.replace('/logo ' ,'')
    text=s.replace(' ', '%20')
    lol = (f"https://single-developers.up.railway.app/logo?name={text}")
    photo = wget.download(lol, 'pythonlogo.png')
    await m.delete()
    caption = f"""
✍️__**Walpaper**__ 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅
◇───────────────◇
🚀 **𝘾𝙧𝙚𝙖𝙩𝙚𝙙 𝘽𝙮** : **{BOT_USERNAME}**
🌺 **𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙧** : ** {message.from_user.mention} **
🍀 **𝙋𝙤𝙬𝙚𝙧𝙙 𝘽𝙮**  : **[◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』](https://t.me/ImGishan)**
◇───────────────◇️  
"""
    await Client.send_photo(message.chat.id, photo=photo, caption=caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•••Telegraph Link•••", url=f"{lol}"
                    )
                ]
            ]
          ),
    )

@Client.on_message(filters.command("logohq"))
async def on_off_antiarab(_, message: Message):
    m = await message.reply_text("**♻ Creating your Logo ♻**......\n\n[░░░░░░░░░░] 00%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇░░░░░░░░] 20%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇░░░░░░] 40%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇░░░░░] 50%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇▇▇░░░] 70%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇▇▇▇░░] 80%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇▇▇▇▇▇] 100%")
    await m.edit("📤Uploading....")
    await m.edit("📤Uploading.....")
    f= message.text
    s=f.replace('/logohq ' ,'')
    text=s.replace(' ', '%20')
    lol = (f"https://single-developers.up.railway.app/logohq?name={text}")
    photo = wget.download(lol, 'pythonlogo.png')
    await m.delete()
    caption = f"""
✍️__**Walpaper**__ 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅
◇───────────────◇
🚀 **𝘾𝙧𝙚𝙖𝙩𝙚𝙙 𝘽𝙮** : **{BOT_USERNAME}**
🌺 **𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙧** : ** {message.from_user.mention} **
🍀 **𝙋𝙤𝙬𝙚𝙧𝙙 𝘽𝙮**  : **[◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』](https://t.me/ImGishan)**
◇───────────────◇️  
"""
    await Client.send_photo(message.chat.id, photo=photo, caption=caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•••Telegraph Link•••", url=f"{lol}"
                    )
                ]
            ]
          ),
    )
@Client.on_message(filters.command("wall"))
async def olol(_, message: Message):
    msg = await Client.send_message(message.chat.id, "🌹 Finding Your Wallpaper..")
    f= message.text
    s=f.replace('/write ' ,'')
    text=s.replace(' ', '%20')
    lol = (f"https://single-developers.up.railway.app/wallpaper?search={text}")
    photo=  wget.download(lol, 'pythonwal.png')
    caption = f"""
✍️__**Walpaper**__ 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅
◇───────────────◇
🚀 **𝘾𝙧𝙚𝙖𝙩𝙚𝙙 𝘽𝙮** : **{BOT_USERNAME}**
🌺 **𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙧** : ** {message.from_user.mention} **
🍀 **𝙋𝙤𝙬𝙚𝙧𝙙 𝘽𝙮**  : **[**◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』**](https://t.me/ImGishan)**
◇───────────────◇️  
"""       
    await msg.delete()
    await Client.send_photo(message.chat.id, photo=photo , caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "••Telegraph Link••", url=f"{lol}"
                    )
                ]
            ]
          ),
    )

@Client.on_message(filters.command("write"))
async def write(_, message: Message):
    m = await message.reply_text("**♻ ✍️Writing your Note ♻**......\n\n[░░░░░░░░░░] 00%")
    await m.edit("**♻ ✍️Writing your Note ♻**......\n\n[▇▇░░░░░░░░] 20%")
    await m.edit("**♻ ✍️Writing your Note ♻**......\n\n[▇▇▇▇░░░░░░] 40%")
    await m.edit("**♻ ✍️Writing your Note ♻**......\n\n[▇▇▇▇▇░░░░░] 50%")
    await m.edit("**♻ ✍️Writing your Note ♻**......\n\n[▇▇▇▇▇▇▇░░░] 70%")
    await m.edit("**♻ ✍️Writing your Note ♻**......\n\n[▇▇▇▇▇▇▇▇░░] 80%")
    await m.edit("**♻ ✍️Writing your Note ♻**......\n\n[▇▇▇▇▇▇▇▇▇▇] 100%")
    await m.edit("📤Uploading....")
    await m.edit("📤Uploading.....")
    f= message.text
    s=f.replace('/write ' ,'')
    text=s.replace(' ', '%20')  
    lol = (f"https://apis.xditya.me/write?text={text}")
    photo=  wget.download(lol ,'img.png')
    caption = f"""
✍️__**Note**__ 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅
◇───────────────◇
🚀 **𝘾𝙧𝙚𝙖𝙩𝙚𝙙 𝘽𝙮** : **{BOT_USERNAME}**
🌺 **𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙧** : ** {message.from_user.mention} **
🍀 **𝙋𝙤𝙬𝙚𝙧𝙙 𝘽𝙮**  : **[◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』](https://t.me/ImGishan)**
◇───────────────◇️
"""       
    await m.delete()
    await Client.send_photo(message.chat.id, photo=photo , caption =caption.format(message.from_user.mention))
    os.remove(photo)     
              
@Client.on_message(filters.command("qr"))
async def qr(_, message: Message):
    m = await message.reply_text("**♻ Generating Qr ♻**......\n\n[░░░░░░░░░░] 00%")
    await m.edit("**♻ Generating Qr ♻**......\n\n[▇▇░░░░░░░░] 20%")
    await m.edit("**♻ Generating Qr ♻**......\n\n[▇▇▇▇░░░░░░] 40%")
    await m.edit("**♻ Generating Qr ♻**......\n\n[▇▇▇▇▇░░░░░] 50%")
    await m.edit("**♻ Generating Qr ♻**......\n\n[▇▇▇▇▇▇▇░░░] 70%")
    await m.edit("**♻ Generating Qr ♻**......\n\n[▇▇▇▇▇▇▇▇░░] 80%")
    await m.edit("**♻ Generating Qr ♻**......\n\n[▇▇▇▇▇▇▇▇▇▇] 100%")
    await m.edit("📤Uploading....")
    await m.edit("📤Uploading.....")
    await m.edit("📤Uploading.......")
    await m.edit("📤Uploading.........")
    f= message.text
    s=f.replace('/qr ' ,'')
    text=s.replace(' ', '%20')  
    lol = (f"https://apis.xditya.me/qr/gen?text={text}")
    photo=  wget.download(lol ,'img.png')
    caption = f"""
✍️__**Note**__ 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅
◇───────────────◇
🚀 **𝘾𝙧𝙚𝙖𝙩𝙚𝙙 𝘽𝙮** : **{BOT_USERNAME}**
🌺 **𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙧** : ** {message.from_user.mention} **
🍀 **𝙋𝙤𝙬𝙚𝙧𝙙 𝘽𝙮**  : **[◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』](https://t.me/ImGishan)**
◇───────────────◇️
"""       
    await m.delete()
    await Client.send_photo(message.chat.id, photo=photo , caption =caption.format(message.from_user.mention))
    os.remove(photo)           
          

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))
          
@Client.on_message(filters.command("song"))
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('🔎 Finding the song...')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)

        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "❌ Found Nothing.\n\nTry another keywork or maybe spell it properly."
        )
        print(str(e))
        return
    m.edit("**📥 Downloading the song......📥**")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = '**~ Uploaded by {BOT_USERNAME} ~**'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        s = message.reply_audio(audio_file, caption=rep, thumb=thumb_name, parse_mode='md', title=title, duration=dur)
        m.delete()
    except Exception as e:
        m.edit('❌ Error')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
 
@Client.on_message(filters.command("send"))
async def qr(bot, update):
    f= update.text
    s=f.replace('/send ' ,'')
    text=s.replace(' ', '%20')
    await Client.send_message(update.chat.id, text=text)
 
@Client.on_message(filters.private & filters.command(["picme"]))
async def help_me(bot, message): 
        reply_markup = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="❣️ ᴘɪᴄ ᴍᴇ ❣️",callback_data="picme")
                 ]]
                  )
        picmeimg = "https://telegra.ph/file/552a7b4454a77b82af9f8.png"
        text = f"""**Now You can Create your Image Useing Me!**
 Pic me : Capture Your Profile Picture.

Send To Inbox Automatically You must start
[This Bot](https://t.me/ImGishan_Bot)

User : {message.from_user.mention}"""

        await message.reply_photo(picmeimg,
        caption=text,
        reply_markup=reply_markup
    )
 
#Callback
 
@Client.on_callback_query()  
async def tgm(bot, update):  
    if update.data == "ref": 
        await update.answer(
             text="♻️Reloading.....♻️",
        )

    elif update.data == "bamk":
         await update.message.edit_text(
             text=START_STRING,
             reply_markup=START_BUTTON,
             disable_web_page_preview=True
         ) 
         await update.answer(
             text="️🍃 ʙᴀᴄᴋ 🍃",
         )
    elif update.data == "tgm":
         await update.message.edit_text(
             text=TELEGRAPH,
             reply_markup=HELPB_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🌻 ᴛᴇʟᴇɢʀᴀᴘʜ 🌻",
         )
    elif update.data == "logoc":
         await update.message.edit_text(
             text=LOGO_STRING,
             reply_markup=HELPB_BUTTON,
             disable_web_page_preview=True
         )  
         await update.answer(
             text="🌻 ʟᴏɢᴏ 🌻",
         ) 
    elif update.data == "pichel":
         await update.message.edit_text(
             text=PIC_HELP,
             reply_markup=HELPB_BUTTON,
             disable_web_page_preview=True
         )  
         await update.answer(
             text="🌻 ᴘɪᴄ ᴍᴇ 🌻",
         )        
    elif update.data == "songg":
         await update.message.edit_text(
             text=SONG_STRING,
             reply_markup=HELPB_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🌻 sᴏɴɢ 🌻", 
         )
    elif update.data == "qrg":
         await update.message.edit_text(
             text=QR_STRING,
             reply_markup=HELPB_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🌻 ǫʀ ɢᴇɴᴇʀᴀᴛᴏʀ 🌻",
         )
    elif update.data == "htgm":
         await update.message.edit_text(
             text=TELEGRAPH,
             reply_markup=HHHELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🌻 ᴛᴇʟᴇɢʀᴀᴘʜ 🌻",
         )
    elif update.data == "hlogoc":
         await update.message.edit_text(
             text=LOGO_STRING,
             reply_markup=HHHELP_BUTTONS,
             disable_web_page_preview=True
         )  
         await update.answer(
             text="🌻 ʟᴏɢᴏ 🌻",
         )         
    elif update.data == "hsongg":
         await update.message.edit_text(
             text=SONG_STRING,
             reply_markup=HHHELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🌻 sᴏɴɢ 🌻",
         )
    elif update.data == "hqrg":
         await update.message.edit_text(
             text=QR_STRING,
             reply_markup=HHHELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🌻 ǫʀ ɢᴇɴᴇʀᴀᴛᴏʀ 🌻",
         )    
    elif update.data == "cmds":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=HELP_BUTTONS,
             disable_web_page_preview=True
         ) 
         await update.answer(
             text="🌴 ʜᴇʟᴘ 🌴",  
         ) 
    elif update.data == "helpb":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=HELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🍃 ʙᴀᴄᴋ 🍃",  
         )
    elif update.data == "hhbak":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=GHELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🍃 ʙᴀᴄᴋ 🍃",  
         )
    elif update.data == "ppbak":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=PICMEH_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🍃 ʙᴀᴄᴋ 🍃",  
         )
    elif update.data == "pbamk":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=PICMEH_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🍃 ʙᴀᴄᴋ 🍃",  
         )
    elif update.data == "helpp":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=PICMEH_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🍃 ʙᴀᴄᴋ 🍃",  
         )
    elif update.data == "ptgm":
         await update.message.edit_text(
             text=TELEGRAPH,
             reply_markup=PICMEB_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🌻 ᴛᴇʟᴇɢʀᴀᴘʜ 🌻",
         )
    elif update.data == "plogoc":
         await update.message.edit_text(
             text=LOGO_STRING,
             reply_markup=PICMEB_BUTTONS,
             disable_web_page_preview=True
         )  
         await update.answer(
             text="🌻 ʟᴏɢᴏ 🌻",
         )         
    elif update.data == "psongg":
         await update.message.edit_text(
             text=SONG_STRING,
             reply_markup=PICMEB_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🌻 sᴏɴɢ 🌻",
         )
    elif update.data == "pqrg":
         await update.message.edit_text(
             text=QR_STRING,
             reply_markup=PICMEB_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🌻 ǫʀ ɢᴇɴᴇʀᴀᴛᴏʀ 🌻",
         )     
    elif update.data == "hcmds":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=GHELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🌴 ʜᴇʟᴘ 🌴",  
         )
    elif update.data == "hbamk":
         text = f"Hi {update.from_user.mention}\n\n**» press the button below to read the explanation and see the list of available commands !**\n\n__⚡️ Powered by ⚡️__[◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』](t.me/imgishan)"
         reply_markup = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="ʜᴇʟᴘ⁉️",callback_data="hcmds")
                 ]]
                 )
         await update.message.edit_text(
             text=text,
             reply_markup=reply_markup,
             disable_web_page_preview=True
         ) 
         await update.answer(
             text="🍃 ʙᴀᴄᴋ 🍃",  
         )
    elif update.data == "ref":
         await update.answer(
             text="♻️Reloading.....♻️",
         )
    elif update.data == "imgi":
         await update.answer(
             text="♻️Reloading.....♻️",
         )
    elif update.data == "picme":
        await update.answer("....🌻 ᴘɪᴄ ᴍᴇ 🌻....\nCapture started...Creating Your dp")
        PICME_TEXT = f"""
**Now You can Create your Image Useing Me!**
 Pic me : Capture Your Profile Picture.

Send To Inbox Automatically You must start
[This Bot](https://t.me/ImGishan_Bot)

User : {update.from_user.mention}
"""
        photoid = update.from_user.photo.big_file_id  
        photo = await bot.download_media(photoid)
        await update.edit_message_media(InputMediaPhoto(media=photo, caption=PICME_TEXT), reply_markup=picmebtns)
        await Client.send_photo(update.from_user.id, photo=photo, caption=PICME_TEXT.format(update.from_user.mention))
        os.remove(photo)
    elif update.data == "add":
         await update.answer(
             text="Adding Soon....",
         )    





         
@Client.on_message(filters.command("addchannel"))
async def sendthepicme(_, message):
    try:
        text = message.text.split(None, 1)[1]
        CHANNEL = text
        picmetxt = f"""
**Now You can Create your Image Useing Me!**
✪ Pic me : Capture Your Profile Picture.

Send To Inbox Automatically You must start
[This Bot](https://t.me/ImGishan_Bot)
Post By : {message.from_user.mention}
"""
        await Client.send_photo(chat_id=CHANNEL,photo="https://telegra.ph/file/490a71ad194e4d6ea95f0.jpg",caption=picmetxt.format(message.from_user.mention), reply_markup=picmebtns)
    except Exception as e:
            await Client.send_message(message.from_user.id,"Please make sure  bot is promoted as admin in your channel.")
            print(str(e)) 


                  

             
         

#PM 

@Client.on_message(filters.private & filters.text)
async def pm_text(bot, message):
    if message.from_user.id == 1884885842:
        await reply_text(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.send_message(
        chat_id=1884885842,
        text=PM_TXT_ATT.format(reference_id, info.first_name, message.text),
        parse_mode="html"
    )

@Client.on_message(filters.private & filters.media)
async def pm_media(bot, message):
    if message.from_user.id == 1884885842:
        await replay_media(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.copy_message(
        chat_id=1884885842,
        from_chat_id=message.chat.id,
        message_id=message.message_id,
        caption=PM_MED_ATT.format(reference_id, info.first_name),
        parse_mode="html"
    )



@Client.on_message(filters.user(1884885842) & filters.text)
async def reply_text(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.send_message(
            text=message.text,
            chat_id=int(reference_id)
        )


@Client.on_message(filters.user(1884885842) & filters.media)
async def replay_media(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.copy_message(
            chat_id=int(reference_id),
            from_chat_id=message.chat.id,
            message_id=message.message_id,
            parse_mode="html"
        ) 

@Client.on_message(filters.user(1884885842) & filters.sticker)
async def replay_media(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.copy_message(
            chat_id=int(reference_id),
            from_chat_id=message.chat.id,
            message_id=message.message_id,
            parse_mode="html"
        ) 
 


lel = 00000000
# pylint:disable=import-error
@Client.on_message(filters.command(["edit", "editor"]))
async def photo(client: Client, message: Message):
    try:
        if not message.reply_to_message.photo:
            await client.send_message(message.chat.id, "Reply to an image please")
            return
    except:
        return
    global lel
    try:
        lel = message.from_user.id
    except:
        return
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text=f"""
Select your required mode from below!
**Designer :** @ImGishan_bot
**Requestor :** {message.from_user.mention}
**Powered By**:@ImGishan 
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="=======================", callback_data="imgi"),
                    ],
                    [
                        InlineKeyboardButton(text="💡 Briget", callback_data="bright"),
                        InlineKeyboardButton(text="🖼 Mixed", callback_data="mix"),
                        InlineKeyboardButton(text="🔳 B&W", callback_data="b|w"),
                    ],
                    [
                        InlineKeyboardButton(text="🟡 Circle", callback_data="circle"),
                        InlineKeyboardButton(text="🩸 Blur", callback_data="blur"),
                        InlineKeyboardButton(text="🌌 Border", callback_data="border"),
                    ],
                    [
                        InlineKeyboardButton(text="🎉 Sticker", callback_data="stick"),
                        InlineKeyboardButton(text="↩️ Rotate", callback_data="rotate"),
                        InlineKeyboardButton(
                            text="🔦 Contrast", callback_data="contrast"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="🌇 Sepia", callback_data="sepia"),
                        InlineKeyboardButton(text="✏️ Pencil", callback_data="pencil"),
                        InlineKeyboardButton(text="🐶 Cartoon", callback_data="cartoon"),
                    ],
                    [
                        InlineKeyboardButton(text="🔄 Invert", callback_data="inverted"),
                        InlineKeyboardButton(text="🔮 Glitch", callback_data="glitch"),
                        InlineKeyboardButton(
                            text="Remove BG 🗑", callback_data="removebg"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text=" Close ✖️", callback_data="close_e"),
                    ],
                    [
                        InlineKeyboardButton(text="=======================", callback_data="imgi"),
                    ],
                ]
            ),
            reply_to_message_id=message.reply_to_message.message_id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text("Something went wrong!", quote=True)
            except Exception:
                return


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    user_id = query.from_user.id
    if lel == user_id:
        if query.data == "removebg":
            await query.message.edit_text(
                "**Select required mode**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="With white BG", callback_data="rmbgwhite"
                            ),
                            InlineKeyboardButton(
                                text="Without BG", callback_data="rmbgplain"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="Sticker", callback_data="rmbgsticker"
                            )
                        ],
                    ]
                ),
            )
        elif query.data == "stick":
            await query.message.edit(
                "**Select a Type**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="Normal", callback_data="stkr"),
                            InlineKeyboardButton(
                                text="Edge Curved", callback_data="cur_ved"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="Circle", callback_data="circle_sticker"
                            )
                        ],
                    ]
                ),
            )
        elif query.data == "rotate":
            await query.message.edit_text(
                "**Select the Degree**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="180", callback_data="180"),
                            InlineKeyboardButton(text="90", callback_data="90"),
                        ],
                        [InlineKeyboardButton(text="270", callback_data="270")],
                    ]
                ),
            )

        elif query.data == "glitch":
            await query.message.edit_text(
                "**Select required mode**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Normal", callback_data="normalglitch"
                            ),
                            InlineKeyboardButton(
                                text="Scan Lines", callback_data="scanlineglitch"
                            ),
                        ]
                    ]
                ),
            )
        elif query.data == "normalglitch":
            await query.message.edit_text(
                "**Select Glitch power level**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="1", callback_data="normalglitch1"
                            ),
                            InlineKeyboardButton(
                                text="2", callback_data="normalglitch2"
                            ),
                            InlineKeyboardButton(
                                text="3", callback_data="normalglitch3"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="4", callback_data="normalglitch4"
                            ),
                            InlineKeyboardButton(
                                text="5", callback_data="normalglitch5"
                            ),
                        ],
                    ]
                ),
            )
        elif query.data == "scanlineglitch":
            await query.message.edit_text(
                "**Select Glitch power level**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="1", callback_data="scanlineglitch1"
                            ),
                            InlineKeyboardButton(
                                text="2", callback_data="scanlineglitch2"
                            ),
                            InlineKeyboardButton(
                                text="3", callback_data="scanlineglitch3"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="4", callback_data="scanlineglitch4"
                            ),
                            InlineKeyboardButton(
                                text="5", callback_data="scanlineglitch5"
                            ),
                        ],
                    ]
                ),
            )
        elif query.data == "blur":
            await query.message.edit(
                "**Select a Type**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="box", callback_data="box"),
                            InlineKeyboardButton(text="normal", callback_data="normal"),
                        ],
                        [InlineKeyboardButton(text="Gaussian", callback_data="gas")],
                    ]
                ),
            )
        elif query.data == "circle":
            await query.message.edit_text(
                "**Select required mode**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="With BG", callback_data="circlewithbg"
                            ),
                            InlineKeyboardButton(
                                text="Without BG", callback_data="circlewithoutbg"
                            ),
                        ]
                    ]
                ),
            )
        elif query.data == "border":
            await query.message.edit(
                "**Select Border**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="🔴 RED 🔴", callback_data="red"),
                            InlineKeyboardButton(
                                text="🟢 Green 🟢", callback_data="green"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="⚫ Black ⚫", callback_data="black"
                            ),
                            InlineKeyboardButton(text="🔵 Blue 🔵", callback_data="blue"),
                        ],
                    ]
                ),
            )

        elif query.data == "bright":
            await query.message.delete()
            await bright(client, query.message)

        elif query.data == "close_e":
            await query.message.delete()

        elif query.data == "mix":
            await query.message.delete()
            await mix(client, query.message)

        elif query.data == "b|w":
            await query.message.delete()
            await black_white(client, query.message)

        elif query.data == "circlewithbg":
            await query.message.delete()
            await circle_with_bg(client, query.message)

        elif query.data == "circlewithoutbg":
            await query.message.delete()
            await circle_without_bg(client, query.message)

        elif query.data == "green":
            await query.message.delete()
            await green_border(client, query.message)

        elif query.data == "blue":
            await query.message.delete()
            await blue_border(client, query.message)

        elif query.data == "red":
            await query.message.delete()
            await red_border(client, query.message)

        elif query.data == "black":
            await query.message.delete()
            await black_border(client, query.message)

        elif query.data == "circle_sticker":
            await query.message.delete()
            await round_sticker(client, query.message)

        elif query.data == "inverted":
            await query.message.delete()
            await inverted(client, query.message)

        elif query.data == "stkr":
            await query.message.delete()
            await sticker(client, query.message)

        elif query.data == "cur_ved":
            await query.message.delete()
            await edge_curved(client, query.message)

        elif query.data == "90":
            await query.message.delete()
            await rotate_90(client, query.message)

        elif query.data == "180":
            await query.message.delete()
            await rotate_180(client, query.message)

        elif query.data == "270":
            await query.message.delete()
            await rotate_270(client, query.message)

        elif query.data == "contrast":
            await query.message.delete()
            await contrast(client, query.message)

        elif query.data == "box":
            await query.message.delete()
            await box_blur(client, query.message)

        elif query.data == "gas":
            await query.message.delete()
            await g_blur(client, query.message)

        elif query.data == "normal":
            await query.message.delete()
            await normal_blur(client, query.message)

        elif query.data == "sepia":
            await query.message.delete()
            await sepia_mode(client, query.message)

        elif query.data == "pencil":
            await query.message.delete()
            await pencil(client, query.message)

        elif query.data == "cartoon":
            await query.message.delete()
            await cartoon(client, query.message)

        elif query.data == "normalglitch1":
            await query.message.delete()
            await normalglitch_1(client, query.message)

        elif query.data == "normalglitch2":
            await query.message.delete()
            await normalglitch_2(client, query.message)

        elif query.data == "normalglitch3":
            await normalglitch_3(client, query.message)

        elif query.data == "normalglitch4":
            await query.message.delete()
            await normalglitch_4(client, query.message)

        elif query.data == "normalglitch5":
            await query.message.delete()
            await normalglitch_5(client, query.message)

        elif query.data == "scanlineglitch1":
            await query.message.delete()
            await scanlineglitch_1(client, query.message)

        elif query.data == "scanlineglitch2":
            await query.message.delete()
            await scanlineglitch_2(client, query.message)

        elif query.data == "scanlineglitch3":
            await query.message.delete()
            await scanlineglitch_3(client, query.message)

        elif query.data == "scanlineglitch4":
            await query.message.delete()
            await scanlineglitch_4(client, query.message)

        elif query.data == "scanlineglitch5":
            await query.message.delete()
            await scanlineglitch_5(client, query.message)

        elif query.data == "rmbgwhite":
            await query.message.delete()
            await removebg_white(client, query.message)

        elif query.data == "rmbgplain":
            await query.message.delete()
            await removebg_plain(client, query.message)

        elif query.data == "rmbgsticker":
            await removebg_sticker(client, query.message)
           
print(f"""
╭━━╮╱╱╱╭━━━┳╮
╰┫┣╯╱╱╱┃╭━╮┃┃
╱┃┃╭╮╭╮┃┃╱┃┃┃╭┳╮╭┳━━╮
╱┃┃┃╰╯┃┃╰━╯┃┃┣┫╰╯┃┃━┫
╭┫┣┫┃┃┃┃╭━╮┃╰┫┣╮╭┫┃━┫
╰━━┻┻┻╯╰╯╱╰┻━┻╯╰╯╰━━╯

Mama Aye Nagitta Puthe
""")
Client.run()
        

