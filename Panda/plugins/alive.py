import time
from platform import python_version

from telethon import version
import asyncio
from Panda import StartTime, pandaversion, PandaBot, SqL, Mongodb, redisalive
pandaub = PandaBot
from ..Config import Config
from ..helpers.functions import get_readable_time, check_data_base_heal_th
from pytgcalls import __version__
from ..core.data import _sudousers_list
from . import mention

CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT = SqL.getdb("CUSTOM_ALIVE_TEXT") or "๊งเผบ Panda Userbot เผป๊ง"

# ================= CONSTANT =================
DEFAULTUSER = mention
# ============================================
EMOJI = SqL.getdb("EMOJI") or "๐จ"
NAME = DEFAULTUSER

plugin_category = "plugins"

SUDO = SqL.getdb("sudoenable")
SUDOuser = _sudousers_list()

LOGO = Config.ALIVE_PIC = SqL.getdb("ALIVE_PIC") or "https://telegra.ph/file/37b52b38dffb858cccf49.jpg"



@PandaBot.ilhammansiz_cmd(
    pattern="alive$",
    command=("alive", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def redis(alive):
    await PandaBot.get_me()
    await get_readable_time((time.time() - StartTime))
    await alive.edit("๊งเผบ Panda Userbot เผป๊ง")
    await alive.edit("๊งเผบ Userbot เผป๊ง")
    await asyncio.sleep(1)
    output = (
        f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        f"โฃโงโงโงโงโงโงโงโงโงโงโงโงโงโงโข\n"
        f"โญโโธโ`๐ข๐๐ป๐ฒ๐ฟ:` {NAME}\n"
        f"โญโโธโ`๐ง๐ฒ๐น๐ฒ๐๐ต๐ผ๐ป:` ๐{version.__version__}\n"
        f"โญโโธโ`๐ฃ๐๐๐ต๐ผ๐ป:` ๐{python_version()}\n"
        f"โญโโธโ`๐ฃ๐๐๐ด๐ฐ๐ฎ๐น๐น๐:` ๐{__version__}\n"
        f"โญโโธโ`๐๐_๐ฆ๐พ๐:` {check_data_base_heal_th()}\n"
        f"โญโโธโ`๐ ๐ผ๐ป๐ด๐ผ_๐๐:` {Mongodb.ping()}\n"
        f"โญโโธโ`๐ฅ๐ฒ๐ฑ๐ถ๐_๐๐:` {redisalive()}\n"
        f"โญโโธโ`๐ฉ๐ฒ๐ฟ๐๐ถ๐ผ๐ป:` ๐{pandaversion}\n"
        f"โญโโธโ`๐ฆ๐๐ฑ๐ผ:` {SUDO}\n"
        f"โฃโงโงโงโงโงโงโงโงโงโงโงโงโงโงโข")
    if LOGO:
        try:
            logo = LOGO
            await alive.delete()
            msg = await PandaBot.send_file(alive.chat_id, logo, caption=output)
            await asyncio.sleep(500)
            await msg.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n *`Logo Yang Disediakan Tidak Valid."
                "\nPastikan Tautan Yang Anda Gunakan Valid`"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(output)
        await asyncio.sleep(100)
        await alive.delete()



