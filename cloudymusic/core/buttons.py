#  Copyright (c) 2025 strad-dev131
#  Licensed under the GNU AGPL v3.0: https://www.gnu.org/licenses/agpl-3.0.html
#  Part of the cloudymusic project. All rights reserved where applicable.


from typing import Literal

from pytdbot import types

from ._config import config


def control_buttons(
    mode: Literal["play", "pause", "resume"],
) -> types.ReplyMarkupInlineKeyboard:
    prefix = "play"
    def btn(text: str, name: str) -> types.InlineKeyboardButton:
        return types.InlineKeyboardButton(
            text=text,
            type=types.InlineKeyboardButtonTypeCallback(f"{prefix}_{name}".encode()),
        )

    skip_btn = btn("‣‣I", "skip")
    stop_btn = btn("▢", "stop")
    pause_btn = btn("II", "pause")
    resume_btn = btn("▷", "resume")
    close_btn = btn("ᴄʟᴏsᴇ", "close")

    layouts = {
        "play": [[skip_btn, stop_btn, pause_btn, resume_btn], [close_btn]],
        "pause": [[skip_btn, stop_btn, resume_btn], [close_btn]],
        "resume": [[skip_btn, stop_btn, pause_btn], [close_btn]],
    }

    return types.ReplyMarkupInlineKeyboard(layouts.get(mode, [[close_btn]]))


CLOSE_BTN = types.InlineKeyboardButton(
    text="Cʟᴏsᴇ", type=types.InlineKeyboardButtonTypeCallback(b"play_close")
)

CHANNEL_BTN = types.InlineKeyboardButton(
    text="ᴜᴘᴅᴀᴛᴇꜱ", type=types.InlineKeyboardButtonTypeUrl(config.SUPPORT_CHANNEL)
)

GROUP_BTN = types.InlineKeyboardButton(
    text="ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", type=types.InlineKeyboardButtonTypeUrl(config.SUPPORT_GROUP)
)

HELP_BTN = types.InlineKeyboardButton(
    text="Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ", type=types.InlineKeyboardButtonTypeCallback(b"help_all")
)

USER_BTN = types.InlineKeyboardButton(
    text="Uꜱᴇʀ Cᴏᴍᴍᴀɴᴅꜱ", type=types.InlineKeyboardButtonTypeCallback(b"help_user")
)

ADMIN_BTN = types.InlineKeyboardButton(
    text="Aᴅᴍɪɴ Cᴏᴍᴍᴀɴᴅꜱ", type=types.InlineKeyboardButtonTypeCallback(b"help_admin")
)

OWNER_BTN = types.InlineKeyboardButton(
    text="Oᴡɴᴇʀ Cᴏᴍᴍᴀɴᴅꜱ", type=types.InlineKeyboardButtonTypeCallback(b"help_owner")
)

DEVS_BTN = types.InlineKeyboardButton(
    text="Dᴇᴠꜱ Cᴏᴍᴍᴀɴᴅꜱ", type=types.InlineKeyboardButtonTypeCallback(b"help_devs")
)

HOME_BTN = types.InlineKeyboardButton(
    text="Hᴏᴍᴇ", type=types.InlineKeyboardButtonTypeCallback(b"help_back")
)

SupportButton = types.ReplyMarkupInlineKeyboard([[CHANNEL_BTN, GROUP_BTN], [CLOSE_BTN]])

HelpMenu = types.ReplyMarkupInlineKeyboard(
    [
        [USER_BTN, ADMIN_BTN],
        [OWNER_BTN, DEVS_BTN],
        [CLOSE_BTN, HOME_BTN],
    ]
)

BackHelpMenu = types.ReplyMarkupInlineKeyboard([[HELP_BTN, HOME_BTN], [CLOSE_BTN]])


# ─────────────────────
# Dynamic Keyboard Generator
# ─────────────────────


def add_me_markup(username: str) -> types.ReplyMarkupInlineKeyboard:
    """
    Returns an inline keyboard with a button to add the bot to a group
    and support buttons.
    """
    return types.ReplyMarkupInlineKeyboard(
        [
            [
                types.InlineKeyboardButton(
                    text="Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                    type=types.InlineKeyboardButtonTypeUrl(
                        f"https://t.me/{username}?startgroup=true"
                    ),
                ),
            ],
            [HELP_BTN],
            [CHANNEL_BTN, GROUP_BTN],
        ]
    )
