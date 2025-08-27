#  Copyright (c) 2025 strad-dev131
#  Licensed under the GNU AGPL v3.0: https://www.gnu.org/licenses/agpl-3.0.html
#  Part of the cloudymusic project. All rights reserved where applicable.

from pytdbot import Client, types

from cloudymusic.core import Filter, chat_cache
from cloudymusic.core.admins import is_admin
from cloudymusic.modules.utils.play_helpers import extract_argument


@Client.on_message(filters=Filter.command("loop"))
async def modify_loop(c: Client, msg: types.Message) -> None:
    """Set loop count for current track (0 to disable)."""
    chat_id = msg.chat_id
    if chat_id > 0:
        return

    if not await is_admin(chat_id, msg.from_id):
        await msg.reply_text("⛔ Administrator privileges required")
        return

    if not chat_cache.is_active(chat_id):
        await msg.reply_text("⏸ No track currently playing")
        return

    args = extract_argument(msg.text, enforce_digit=True)
    if not args:
        await msg.reply_text(
            "🔁 <b>Loop Control</b>\n\n"
            "Usage: <code>/loop [count]</code>\n"
            "• 0 - Disable loop\n"
            "• 1-10 - Loop count"
        )
        return

    loop = int(args)
    if loop < 0 or loop > 10:
        await msg.reply_text("⚠️ Loop count must be between 0 and 10")
        return

    chat_cache.set_loop_count(chat_id, loop)

    action = "Looping disabled" if loop == 0 else f"Set to loop {loop} time(s)"
    reply = await msg.reply_text(
        f"🔁 {action}\n" f"└ Changed by: {await msg.mention()}"
    )
    if isinstance(reply, types.Error):
        c.logger.warning(f"⚠️ Failed to send reply: {reply.message}")
