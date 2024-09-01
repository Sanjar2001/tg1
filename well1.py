# import asyncio
# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters.command import Command
# import os
#
# # Configure logging
# logging.basicConfig(level=logging.INFO)
#
# # Bot token can be obtained via @BotFather
# TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")
#
# # All handlers should be attached to the Router (or Dispatcher)
# dp = Dispatcher()
#
# @dp.message(Command(commands=["start", "help"]))
# async def command_start_handler(message: types.Message):
#     await message.answer("Hi! I'm an echo bot. Send me any message!")
#
# @dp.message()
# async def echo_handler(message: types.Message):
#     response = f"\"{message.text}\" - that's what she said."
#     await message.answer(response)
#
# async def main():
#     bot = Bot(TOKEN)
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())


# import asyncio
# from aiogram import Bot, Dispatcher, Router
# from aiogram.types import Message
#
# # Инициализация маршрутизатора
# router = Router()
#
# # Обработчик сообщения
# @router.message()
# async def greet_user(message: Message):
#     language_code = message.from_user.language_code
#     await message.answer(f"Привет! Твой языковой код: {language_code}")
#
# # Основная функция для запуска бота
# async def main():
#     bot = Bot(token='YOUR_BOT_TOKEN_HERE')
#     dp = Dispatcher()
#     dp.include_router(router)
#     await dp.start_polling(bot)
#
# # Запуск бота
# if __name__ == '__main__':
#     asyncio.run(main())


# import asyncio
# from aiogram import Bot, Dispatcher, Router, F
# from aiogram.types import Message
#
# # Инициализация маршрутизатора
# router = Router()
#
# # Функция для обработки сообщений "Hi", "Hello" и "What's up"
# @router.message(F.text.in_({"Hi", "Hello", "What's up"}))
# async def say_hi(message: Message):
#     username = message.from_user.first_name
#     await message.answer(f"Hey, {username}!")
#
# # Основной обработчик сообщений
# @router.message()
# async def echo_message(message: Message):
#     user_text = message.text
#     await message.answer(f"You said: {user_text}")
#
# # Основная функция для запуска бота
# async def main():
#     bot = Bot(token='YOUR_BOT_TOKEN_HERE')
#     dp = Dispatcher()
#     dp.include_router(router)
#     await dp.start_polling(bot)
#
# # Запуск бота
# if __name__ == '__main__':
#     asyncio.run(main())

# import asyncio
# import re
# from aiogram import Bot, Dispatcher, Router, F
# from aiogram.types import Message
#
# # Инициализация маршрутизатора
# router = Router()
#
# # Функция для обработки сообщений "Hi", "Hello" и "What's up"
# @router.message(F.text.in_({"Hi", "Hello", "What's up"}))
# async def say_hi(message: Message):
#     username = message.from_user.first_name
#     await message.answer(f"Hey, {username}!")
#
# # Функция для обработки математических выражений
# @router.message(F.text.regexp(r'^\d+\s*[\+\-\*/]\s*\d+$'))
# async def calculate(message: Message):
#     expression = message.text.replace(" ", "")
#     try:
#         # Используем eval для вычисления результата
#         result = eval(expression)
#         await message.answer(f"{expression} = {result}")
#     except Exception:
#         await message.answer("Ошибка в вычислении. Пожалуйста, проверьте ввод.")
#
# # Основной обработчик сообщений
# @router.message()
# async def echo_message(message: Message):
#     user_text = message.text
#     await message.answer(f"You said: {user_text}")
#
# # Основная функция для запуска бота
# async def main():
#     bot = Bot(token='YOUR_BOT_TOKEN_HERE')
#     dp = Dispatcher()
#     dp.include_router(router)
#     await dp.start_polling(bot)
#
# # Запуск бота
# if __name__ == '__main__':
#     asyncio.run(main())

