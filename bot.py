import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME"))
GROUPS = []
for grp in environ.get("GROUPS").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS").split():
    ADMINS.append(int(usr))

START_MSG = "<b>ʜɪ 👋 {},\n\n➠ ɪ'ᴍ ᴀ ꜱɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ\n\n➠ ɪ ᴄᴀɴ ᴅᴇʟᴇᴛᴇ 🚮 ɢʀᴏᴜᴘ ᴍᴇꜱꜱᴀɢᴇ ᴀꜰᴛᴇʀ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ᴏꜰ ᴛɪᴍᴇ ⏰\n\n➠ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀꜱ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴅᴇʟᴇᴛᴇ ᴍᴇꜱꜱᴀɢᴇ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ᴀꜱ ᴡᴇʟʟ ᴀꜱ ᴀᴄᴄᴏᴜɴᴛ ʏᴏᴜ ᴜꜱᴇᴅ ᴛᴏ ᴄʀᴇᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀꜱ ᴀ ᴍᴇᴍʙᴇʀ ᴏꜰ ᴛʜᴀᴛ ɢʀᴏᴜᴘ\n\n➠ ᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ : @ChVivekTomar</b>"


User = Client(session_name=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(session_name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.message_id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
