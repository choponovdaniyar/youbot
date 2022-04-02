from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .callback_data import quality_callback
quality = InlineKeyboardMarkup()

async def push_quality(mp, cb):
    global quality
    quality = InlineKeyboardMarkup()
    for x in mp:
        try:
            btn = InlineKeyboardButton(
                text=x, 
                callback_data=quality_callback.new(
                    quality = x,
                    url = cb
                )
            )
            quality.add(btn)
        except ValueError:
            btn = InlineKeyboardButton(
                text=x, 
                callback_data=quality_callback.new(
                    quality = x,
                    url = cb[8:]
                )
            )
            quality.add(btn)
            