from aiogram import types
from aiogram import asyncio
from aiogram.utils.exceptions import MessageNotModified
from aiogram.dispatcher import FSMContext
from keyboards.inline import callback_data, quality

from loader import dp, bot
from data.scripts import mytubesave, linkshorter

import random



@dp.message_handler()
async def bot_echos(message: types.Message):
    yousave = mytubesave.YouSave(message.text)
    if yousave.video == None:
        await message.answer(
            "⚠️ Не правильный формат ссылки. "
            "Отправь 🔗 ссылку на видео YouTube!")
    else:
        links = await yousave.get_video()  
        await quality.push_quality(links.keys(), message.text)
        
        await bot.send_photo(
            message.chat.id, 
            types.InputFile.from_url(
                url = await yousave.get_imgUrl(),
                filename ="Изображение"
            ),
            "<b>Название:</b> {}\n\n<b>Автор:</b> {}".format(await yousave.get_title(), await yousave.get_author()),
            reply_markup = quality.quality
        )



@dp.callback_query_handler(callback_data.quality_callback.filter())
async def get_videos(call: types.CallbackQuery, callback_data: dict):
    await bot.delete_message(
        chat_id=call.from_user.id, 
        message_id= call.message.message_id
    )
    yousave = mytubesave.YouSave(callback_data["url"])
    links = await yousave.get_video()

    v = '█'
    message_wait  = await call.message.answer("<b>|{}|</b>".format("   " * 20))
    progressbar = 0
    while progressbar < 100:
        progressbar = min(100,progressbar + random.randint(1 * 5,8 * 5))
        try:
            await message_wait.edit_text(
                text = "<b>|{}|</b> {}%".format( v*(progressbar // 5) + "   "*(20 - progressbar // 5), progressbar)
            )
        except MessageNotModified:
            pass
        await asyncio.sleep(1/10)

    for x in links:
        if callback_data["quality"] == x:
            link = await linkshorter.get_shortLink(links[x])
            break

    await bot.delete_message(
        chat_id=call.from_user.id, 
        message_id=message_wait.message_id
    )

    await bot.send_message(
        call.message.chat.id,"💾 Нажмите <a href='{}'>сюда</a>, чтобы перейти на страницу для скачивания".format(link) 
    )
            