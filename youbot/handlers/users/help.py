from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд:\n",
            "/start - Начать диалог\n\n",
            "🔗Отравьте ссылку для загрузки видео")
    
    await message.answer("\n".join(text))
