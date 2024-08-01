# module_13_4 Клавиатура кнопок.

'''
Задача "Меньше текста, больше кликов":
Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах тела для расчёта калорий выдавались по нажатию
кнопки.

    Измените massage_handler для функции set_age. Теперь этот хэндлер будет реагировать на текст 'Рассчитать', а не на
    'Calories'.
    Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом: 'Рассчитать' и
    'Информация'. Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства при помощи параметра
    resize_keyboard.
    Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.

В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками. При нажатии на кнопку с надписью
'Рассчитать' срабатывает функция set_age с которой начинается работа машины состояний для age, growth и weight.
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

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать!")
    await message.answer("Это бот по задаче module_13_5 для вычисления потребности в калориях для мужчин",
    reply_markup=create_keyboard())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = create_keyboard()
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text.lower() == 'рассчитать')
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


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
    # Сохранение веса
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