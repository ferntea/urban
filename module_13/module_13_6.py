# module_13_3 Методы отправки сообщений.

'''
Задача "Ещё больше выбора":
Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать' присылалась Inline-клавиатруа.
Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:

    С текстом 'Рассчитать норму калорий' и callback_data='calories'
    С текстом 'Формулы расчёта' и callback_data='formulas'

Создайте новую функцию main_menu(message), которая:

    Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
    Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'

Создайте новую функцию get_formulas(call), которая:

    Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
    Будет присылать сообщение с формулой Миффлина-Сан Жеора.

Измените функцию set_age и декоратор для неё:

    Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
    Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.

По итогу получится следующий алгоритм:

    Вводится команда /start
    На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
    В ответ на кнопку 'Рассчитать' присылается Inline меню: 'Рассчитать норму калорий' и 'Формулы расчёта'
    По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
    По Inline кнопке 'Рассчитать норму калорий' начинает работать машина состояний по цепочке.
'''

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from module_13_config import API

bot = Bot(token=API)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

def create_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_calculate = types.KeyboardButton("Рассчитать")
    button_info = types.KeyboardButton("Информация")
    keyboard.add(button_calculate, button_info)
    return keyboard

def create_inline_keyboard():
    inline_keyboard = types.InlineKeyboardMarkup()
    button_calories = types.InlineKeyboardButton("Рассчитать норму калорий", callback_data='calories')
    button_formulas = types.InlineKeyboardButton("Формулы расчёта", callback_data='formulas')
    inline_keyboard.add(button_calories, button_formulas)
    return inline_keyboard

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать!", reply_markup=create_keyboard())
    # await message.answer("Это бот по задаче module_13_6 для вычисления потребности в калориях для мужчин",
    #                     reply_markup=create_keyboard())

@dp.message_handler(lambda message: message.text.lower() == 'рассчитать')
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=create_inline_keyboard())

@dp.message_handler(lambda message: message.text.lower() == 'информация')
async def main_menu(message: types.Message):
    await message.answer("Это бот по задаче module_13_6 для вычисления потребности в калориях для мужчин")

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula_message = (
        "Формула Миффлина - Сан Жеора для мужчин:\n"
        "BMR = 10 * вес + 6.25 * рост - 5 * возраст + 5"
    )
    await call.message.answer(formula_message)
    await call.answer()

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)

    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def process_growth(message: types.Message, state: FSMContext):
    growth = message.text
    await state.update_data(growth=growth)

    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def process_weight(message: types.Message, state: FSMContext):
    weight = message.text
    await state.update_data(weight=weight)

    user_data = await state.get_data()
    age = int(user_data.get('age', 0))
    growth = int(user_data.get('growth', 0))
    weight = int(user_data.get('weight', 0))

    # Формула Миффлина - Сан Жеора для мужчин: BMR = 10 * weight + 6.25 * height - 5 * age + 5
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал в день.")

    await state.finish()  # Завершение машины состояний


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
