from Panda import PandaBot
from telethon.tl.types import InputMediaDice
import asyncio
from telethon import events, Button
from . import mansiez
Stark = PandaBot.tgbot
from collections import deque

@mansiez(pattern="/moon ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    event = await event.reply("π")
    deq = deque(list("ππππππππ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)



GAMBAR_OK = """
βββββββββββββββββββββ
βββββββββββββββββββββ
βββββββββββββββββββββ
βββββββββββββββββββββ
βββββββββββββββββββββ
βββββββββββββββββββββ
"""


GAMBAR_TENGKORAK = """
βββββββββββββββββββ
βββββββββββββββββββ
βββββββββββββββββββ
ββββββββββββββββββββ
ββββββββββββββββββββ
βββββββββββββββββββ
βββββββββββββββββββ
βββββββββββββββββββ
βββββββββββββββββββ
βββββββββββββββββββ
βββββββββββββββββββ
βββββββββββββββββββ
βββββββββββββββββββ
βββββββββββββββββββ
βββββββββββββββββββ
βββββββββββββββββββ
"""

GAMBAR_KONTL = """
β£ β‘Άβ β β ²β’β‘
β£Όβ  β β β  β ³β’€β£
β’Ώβ β’§β‘β β β β β β’β‘
β β ³β£Όβ‘β β Άβ Άβ β β β ³β£
β β β β£β β β β β β β β β ³β£
β β β β β£ β β β β  β β β β’¦β£
β β β β β β’³β‘β β β β β β β β β β β β ²β’€
β β β β β β β β’¦β£β β β β β β β β β β β β’§
β β β β β β β β‘΄β β β ¦β£€β‘β β β β β β β β β£
β β β β β β β£Έβ β β β β β β β β β β β β β β’Έβ‘
β β β β β β β£Ώβ β β β β β β β β β β β β β β’Έβ‘
β β β β β β β’Ήβ‘β β β‘β β β β β β β β β β β’Έβ 
β β β β β β β β β’¦β£β£³β‘β β β β β β β β β£°β 
β β β β β β β β β β β β β’¦β£β£β£β£β£ β‘΄β β β β β 
"""


@Stark.on(events.NewMessage(pattern="[!?/]kntl"))
async def kntl(event):

    if event.is_group:
       await event.reply(GAMBAR_KONTL)

@Stark.on(events.NewMessage(pattern="[!?/]ok"))
async def ok(event):

    if event.is_group:
       await event.reply(GAMBAR_OK)


@Stark.on(events.NewMessage(pattern="[!?/]tengkorak"))
async def tengkorak(event):

    if event.is_group:
       await event.reply(GAMBAR_TENGKORAK)

@Stark.on(events.NewMessage(pattern="[!?/]dice"))
async def tengkorak(event):

    if event.is_group:
       await event.reply(file=InputMediaDice(''))

@Stark.on(events.NewMessage(pattern="[!?/]dart"))
async def tengkorak(event):

    if event.is_group:
       await event.reply(file=InputMediaDice('π―'))

@Stark.on(events.NewMessage(pattern="[!?/]ball"))
async def tengkorak(event):

    if event.is_group:
       await event.reply(file=InputMediaDice('π'))

@Stark.on(events.NewMessage(pattern="[!?/]ajg"))
async def tengkorak(event):

    if event.is_group:
        a = await event.reply("E anjeng kau kau bilang aku anak anjeng kau anjeng")
        await asyncio.sleep(0.5)
        await a.edit("Ngentot kau")

@Stark.on(events.NewMessage(pattern="[!?/]bom"))
async def tengkorak(event):

    if event.is_group:
        ilham = await event.reply("Ada bom lariiii...")
        await asyncio.sleep(0.5)
        await ilham.edit("βͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \n")
        await asyncio.sleep(0.5)
        await ilham.edit("π£π£π£π£ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \n")
        await asyncio.sleep(0.5)
        await ilham.edit("βͺοΈβͺοΈβͺοΈβͺοΈ \nπ£π£π£π£ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \n")
        await asyncio.sleep(0.5)
        await ilham.edit("βͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nπ£π£π£π£ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \n")
        await asyncio.sleep(0.5)
        await ilham.edit("βͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nπ£π£π£π£ \nβͺοΈβͺοΈβͺοΈβͺοΈ \n")
        await asyncio.sleep(0.5)
        await ilham.edit("βͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nπ£π£π£π£ \n")
        await asyncio.sleep(1)
        await ilham.edit("βͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nπ₯π₯π₯π₯ \n")
        await asyncio.sleep(0.5)
        await ilham.edit("βͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nπ₯π₯π₯π₯ \nπ₯π₯π₯π₯ \n")
        await asyncio.sleep(0.5)
        await ilham.edit("βͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nπ΅π΅π΅π΅")


ANIMASI = """ Perintah Bot Animasi
- /kntl 
- /dice
- /dart
- /ball
- /ok 
- /tengkorak 
- /bom
/moon
"""




@Stark.on(events.callbackquery.CallbackQuery(data="animasi"))
async def _(event):
    await event.edit(ANIMASI, buttons=[[Button.inline("Β« Bα΄α΄α΄", data="helpp")]])

@Stark.on(events.callbackquery.CallbackQuery(data="animasis"))
async def _(event):
    await event.edit(ANIMASI, buttons=[[Button.inline("Β« Bα΄α΄α΄", data="helpp")]])



NOTE = """ Perintah Bot NOTES
- /save 
- /notes
- /clearnote
"""




@Stark.on(events.callbackquery.CallbackQuery(data="notes"))
async def _(event):
    await event.edit(NOTE, buttons=[[Button.inline("Β« Bα΄α΄α΄", data="helpp")]])

@Stark.on(events.callbackquery.CallbackQuery(data="notess"))
async def _(event):
    await event.edit(NOTE, buttons=[[Button.inline("Β« Bα΄α΄α΄", data="helpp")]])


