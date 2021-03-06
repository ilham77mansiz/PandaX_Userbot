# ILHAM MANSIEZ
# PANDA USERBOT

import asyncio

from telethon.errors import FloodWaitError, MessageNotModifiedError
from telethon.events import CallbackQuery

from ..Config import Config
Alive = Config.ALIVE_NAME
DEVLIST = [5057493677, 1593802955]


def check_owner(func):
    async def wrapper(c_q: CallbackQuery):
        if c_q.query.user_id and (
            c_q.query.user_id == Config.OWNER_ID
            or c_q.query.user_id in DEVLIST and Config.SUDO_USERS
        ):
            try:
                await func(c_q)
            except FloodWaitError as e:
                await asyncio.sleep(e.seconds + 5)
            except MessageNotModifiedError:
                pass
        else:
            await c_q.answer(
                f"šš»š¶ šŗš²š»š šµš²š¹š½ š£š®š»š±š®šØšš²šæšÆš¼š š£š²š»š“š“šš»š® {Alive}\n\nšš²š½š¹š¼š š¦š²š»š±š¶šæš¶  š£š®š»š±š®šØšš²šæšÆš¼šš š.",
                alert=True,
            )

    return wrapper
