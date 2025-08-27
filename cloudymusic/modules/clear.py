#  Copyright (c) 2025 strad-dev131
#  Licensed under the GNU AGPL v3.0: https://www.gnu.org/licenses/agpl-3.0.html
#  Part of the cloudymusic project. All rights reserved where applicable.

from pytdbot import Client, types

from cloudymusic.core import Filter, chat_cache
from cloudymusic.core.admins import is_admin


@Client.on_message(filters=Filter.command("clear"))
async def clear_queue(c: Client, msg: types.Message) -> None:
    """Clear the current playback queue."""
    chat_id = msg.chat_id

    if chat_id > 0:
        return None

    if not await is_admin(chat_id, msg.from_id):
        await msg.reply_text("⛔ Administrator privileges required.")
        return None

    if not chat_cache.is_active(chat_id):
        await msg.reply_text("ℹ️ No active playback session found.")
        return None

    if not chat_cache.get_queue(chat_id):
        await msg.reply_text("ℹ️ The queue is already empty.")
        return None

    chat_cache.clear_chat(chat_id)
    reply = await msg.reply_text(f"✅ Queue cleared by {await msg.mention()}")
    if isinstance(reply, types.Error):
        c.logger.warning(f"Error sending reply: {reply}")
    return None
