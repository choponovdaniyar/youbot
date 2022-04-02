from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        '👋 Привет!\n\n'
        '⬇️Я умею скачивать видео из YouTube.\n'
        'Чтобы скачать видео, отправьте 🔗 ссылку на видео.\n\n'
    )
