import g4f
import asyncio
from aiogram import Dispatcher, Bot, types
from aiogram.filters import CommandStart

token = '6704974378:AAGmoZPMpLLFVqPEPfWQnK8HN2BPE-32Obc'
g4f.debug.logging = True
g4f.check_version = False

message_storage = {}


def split_string(input_string, chunk_size):
    return [input_string[i:i+chunk_size] for i in range(0, len(input_string), chunk_size)]


async def start_bot(bot: Bot):
    await bot.send_message(1392464735, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(1392464735, text='Бот завершил свою работу!')


async def gpt(message: types.Message):
    await message.bot.send_chat_action(message.chat.id, 'typing')
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.gpt_35_turbo,
            provider=g4f.Provider.You,
            messages=message_storage[message.from_user.id]
        )
        message_storage[message.from_user.id].append({'role': 'user', 'content': message.text})
        message_storage[message.from_user.id].append({'role': 'assistant', 'content': response})
        for item in split_string(response, 4096):
            await message.reply(item)
    except Exception as e:
        await message.reply(f'Я не могу ответить на этот вопрос, по причине: {e}')


async def start():
    bot = Bot(token)

    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    
    @dp.message(CommandStart())
    async def start(message: types.Message):
        await message.answer('Привет, я готов отвечать на твои запросы!')
    
    dp.message.register(gpt)

    try:
        await dp.start_polling(bot)
    finally:
        stop_bot(bot)
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
