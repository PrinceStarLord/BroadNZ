import os
import traceback
import logging

from pyrogram import Client
from pyrogram import StopPropagation, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

import config
from handlers.broadcast import broadcast
from handlers.check_user import handle_user_status
from handlers.database import Database

LOG_CHANNEL = config.LOG_CHANNEL
AUTH_USERS = config.AUTH_USERS
DB_URL = config.DB_URL
DB_NAME = config.DB_NAME

db = Database(DB_URL, DB_NAME)


Bot = Client(
    "BroadcastBot",
    bot_token=config.BOT_TOKEN,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
)

@Bot.on_message(filters.private)
async def _(bot, cmd):
    await handle_user_status(bot, cmd)

@Bot.on_message(filters.private & filters.command("broadcast"))
async def broadcast_handler_open(_, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if m.reply_to_message is None:
        await m.delete()
    else:
        await broadcast(m, db)


@Bot.on_message(filters.private & filters.command("stats"))
async def sts(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    await m.reply_text(
        text=f"**TOTAL USERS :** `{await db.total_users_count()}`\n\n**Total Users, Notification Enabled 🔔 :** `{await db.total_notif_users_count()}`",
        quote=True
    )

# @Bot.on_callback_query()
# async def callback_handlers(bot: Client, cb: CallbackQuery):
#     user_id = cb.from_user.id
#     if cb.data == "notifon":
#         notif = await db.get_notif(cb.from_user.id)
#         if notif is True:
#             await db.set_notif(user_id, notif=False)
#         else:
#             await db.set_notif(user_id, notif=True)
#         await cb.message.edit(
#             f"`Here You Can Set Your Settings:`\n\nSuccessfully setted notifications to **{await db.get_notif(user_id)}**",
#             reply_markup=InlineKeyboardMarkup(
#                 [
#                     [
#                         InlineKeyboardButton(
#                             f"NOTIFICATION  {'🔔' if ((await db.get_notif(user_id)) is True) else '🔕'}",
#                             callback_data="notifon",
#                         )
#                     ],
#                     [InlineKeyboardButton("❎", callback_data="closeMeh")],
#                 ]
#             ),
#         )
#         await cb.answer(
#             f"Successfully setted notifications to {await db.get_notif(user_id)}"
#         )
#     else:
#         await cb.message.delete(True)


Bot.run()
