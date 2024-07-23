# module_13_3 Методы отправки сообщений.

'''
Задача "Он мне ответил!":
Измените функции start и all_messages так, чтобы вместо вывода в консоль строки отправлялись в чате телеграм.
Запустите ваш Telegram-бот и проверьте его на работоспособность.
Пример результата выполнения программы:
    Привет!
    Введите команду /start, чтобы начать общение
    /start
    Привет! Я бот, помогающий твоему здоровью

Примечания:

    Для ответа на сообщение запускайте метод answer асинхронно.
    При отправке вашего кода на GitHub не забудьте убрать ключ для подключения к вашему боту!
'''

from aiogram import Bot, Dispatcher, executor, types
import asyncio

api =
bot = Bot(token=api)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_messages(message):
    print("Start message")
    await message.answer("Привет! Я бот, помогающий твоему здоровью")

@dp.message_handler()
async def all_messages(message: types.Message):
    print("Введите команду /start, чтобы начать общение!")
    await message.answer("Введите команду /start, чтобы начать общение!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)