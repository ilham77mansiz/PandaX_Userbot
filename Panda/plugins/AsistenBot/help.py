from telethon import events, Button
from Panda import PandaBot
bot = PandaBot.tgbot
X = "https://telegra.ph/file/695cb726224d2a7037399.jpg"
from Panda.modules import mention
owner = "https://t.me/diemmmmmmmmmm"
support = "https://t.me/TeamSquadUserbotSupport"
btn =[
    [Button.inline("๐ Notes ๐", data="notes"), Button.inline("๐ผ Animation ๐ผ", data="animasi")],
    [Button.inline("๐คก Admin ๐คก", data="admin"), Button.inline("๐ท Bans ๐ท", data="bans")],
    [Button.inline(" ๐Pins ๐", data="pins"), Button.inline("๐ Pugres ๐", data="purges")],
    [Button.inline("๐ Locks ๐", data="locks"), Button.inline("๐ Misc ๐", data="misc")],
    [Button.inline("๐งโโ๏ธ Zombies ๐งโโ๏ธ", data="zombies"), Button.inline("๐จ Telegraph ๐จ", data="telegram")],
    [Button.inline("๐ Tiny ๐", data="tiny"), Button.inline("๐ Covid ๐", data="covid")],
    [Button.inline("๐ ZonaDewasa ๐", data="payudara"), Button.inline("๐ฎ๐ฉ Country ๐ฎ๐ฉ", data="negara")],
    [Button.inline("๐ TTS ๐", data="tts"), Button.inline("๐ Heroku ๐", data="heroku")],
    [Button.inline("๐ซ Close ๐ซ", data="closeit")]]

helpn =[
    [Button.inline("๐ Notes ๐", data="notess"), Button.inline("๐ผ Animation ๐ผ", data="animasis")],
    [Button.inline("๐คก Admin ๐คก", data="admins"), Button.inline("๐ท Bans ๐ท", data="banss")],
    [Button.inline(" ๐Pins ๐", data="pinss"), Button.inline("๐ Pugres ๐", data="purgess")],
    [Button.inline("๐ Locks ๐", data="lockss"), Button.inline("๐ Misc ๐", data="miscs")],
    [Button.inline("๐งโโ๏ธ Zombies ๐งโโ๏ธ", data="zombiess"), Button.inline("๐จ Telegraph ๐จ", data="telegrams")],
    [Button.inline("๐ Tiny ๐", data="tinys"), Button.inline("๐ Covid ๐", data="covids")],
    [Button.inline("๐ ZonaDewasa ๐", data="payudaras"), Button.inline("๐ฎ๐ฉ Country ๐ฎ๐ฉ", data="negaras")],
    [Button.inline("๐ TTS ๐", data="tts"), Button.inline("๐ Heroku ๐", data="herokus")],
    [Button.inline("๐? Menu Utama ๐?", data="mainmenu")],
    [Button.inline("๐ซ Close ๐ซ", data="closeit")]]

HELP_TEXT = f"""
**Hello ๐\nSaya Asistennya bot: {mention}\nIni Tombol Menu Help Asisten PandaX_Userbot:**

Support** [UserBotSupport]({support})**
"""


@bot.on(events.NewMessage(pattern=("/help")))
async def alive(event):
  await Stark.send_message(event.chat, HELP_TEXT, file=X, buttons=btn)



@bot.on(events.callbackquery.CallbackQuery(data="helpp"))
async def _(event):

     await event.edit(HELP_TEXT, buttons=btn)


@bot.on(events.callbackquery.CallbackQuery(data="helpbot"))
async def _(event):

     await event.edit(HELP_TEXT, buttons=helpn)
