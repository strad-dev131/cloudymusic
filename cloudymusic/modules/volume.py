#  Copyright (c) 2025 strad-dev131
#  Licensed under the GNU AGPL v3.0: https://www.gnu.org/licenses/agpl-3.0.html
#  Part of the cloudymusic project. All rights reserved where applicable.

from pytdbot import Client, types

from cloudymusic.core import Filter, call
from .funcs import is_admin_or_reply
from .utils.play_helpers import extract_argument


@Client.on_message(filters=Filter.command(["volume", "cvolume"]))
async def volume(c: Client, msg: types.Message) -> None:
    """Adjust the playback volume (1-200%)."""
    chat_id = await is_admin_or_reply(msg)
    if isinstance(chat_id, types.Error):
        c.logger.warning(f"⚠️ Admin check failed: {chat_id.message}")
        return None

    if isinstance(chat_id, types.Message):
        return None

    args = extract_argument(msg.text, enforce_digit=True)
    if not args:
        await msg.reply_text(
            "🔊 <b>Volume Control</b>\n\n"
            "Usage: <code>/volume [1-200]</code>\n"
            "Example: <code>/volume 80</code> for 80% volume\n"
            "Use <code>/volume 0</code> to mute"
        )
        return None

    try:
        vol_int = int(args)
    except ValueError:
        await msg.reply_text("⚠️ Please enter a valid number between 1 and 200")
        return None

    if vol_int == 0:
        await msg.reply_text(f"🔇 Playback muted by {await msg.mention()}")
        return None

    if not 1 <= vol_int <= 200:
        await msg.reply_text("⚠️ Volume must be between 1% and 200%")
        return None

    done = await call.change_volume(chat_id, vol_int)
    if isinstance(done, types.Error):
        await msg.reply_text(f"⚠️ <b>Error:</b> {done.message}")
        return None

    await msg.reply_text(f"🔊 Volume set to <b>{vol_int}%</b> by {await msg.mention()}")
    return None
