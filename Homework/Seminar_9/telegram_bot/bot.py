import logging
from aiogram import Bot, Dispatcher, executor, types
import db, bot_command, pytube

token_bot = db.get_token()

bot = Bot(token=token_bot)
dp = Dispatcher(bot)

download = False
link = ''
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("""Вас приветствует @my_yt_download_video_bot.
    Он умеет загружать видео с ютюба по ссылке.
    Для этого достаточно отправить ссылку на интересующее Вас видео""")


@dp.message_handler(commands="load")
async def cmd_load(message: types.Message):
    await message.answer('Введите url видео')


@dp.message_handler(commands="hello")
async def cmd_test1(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f'Привет, {user_name}')


@dp.message_handler() 
async def cmd_user_message(message: types.Message):
    global download, link
    if 'https://' in message.text:
        # url = message.text
        link = await bot_command.get_link(message.text)
        await message.answer('Введите номер необходимого качества')
        quality_video = await quality(link)
        for i in quality_video:
            await message.answer(i)
        download = True
    elif download:
        number_quality = message.text
        download = False
        await bot_command.load(link, number_quality)


async def quality(link):

    list_stream = []
    for i in link.streams.filter(progressive='True'):
        list_stream.append(str(i))

    buff = []
    for i in list_stream:
        i = i[9:-1].split()
        dict_streams = {}
        for k in range(len(i)):
            j = i[k].split('=')
            dict_streams[j[0]] = j[1].replace('"', '') 
        
        buff.append(dict_streams)
    res_list = []
    for i in buff:
        itag = i['itag']
        res = i['res']
        fps = i['fps']
        res_list.append(f'{itag} - {res} {fps}')
    return res_list    


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
