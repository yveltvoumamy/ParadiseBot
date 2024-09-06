from aiogram import F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, FSInputFile, InputMediaPhoto
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

import os
from pathlib import Path

from src.bot_handler.bot import bot, dp
from src.bot_handler.keyboards.menu_keyboard import start_menu_keyboard, next_step_menu_keyboard
from src.data.file_manager import get_str_from_txt

from src.bot_handler.handlers.buy_ticket_handler import *

async def main() -> None:
    await dp.start_polling(bot)

async def edit_message(message: Message, text: str, keyboard: InlineKeyboardMarkup):
    try:
        await bot.edit_message_text(text=text, chat_id=message.chat.id,
                                    message_id=message.message_id)
        await bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=mesage.message_id,
                                            reply_markup=keyboard)
    except Exception as e:
        if "message can't be edited" in str(e):
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            await message.answer(text, reply_markup=keyboard)

@dp.message(CommandStart())
async def process_start(message: Message) -> None:
    photo = 'AgACAgIAAxkDAAMpZtro7cUlU_0taPfUxIg9cQM6n8oAAsPiMRvMb9hKJkkcOZWgqRUBAAMCAAN5AAM2BA'
    text = await get_str_from_txt(Path('src', 'data', 'messages', 'menu_message', 'menu_text.txt'))
    keyboard = start_menu_keyboard
    await message.answer_photo(photo=photo, caption=text, reply_markup=keyboard)
    # print(msg_id.photo[-1].file_id)


@dp.callback_query(F.data == 'menu')
async def process_back_to_menu(callback_query: CallbackQuery) -> None:
    # очистить фсм
    await callback_query.answer(f'')
    message = callback_query.message
    photo = 'AgACAgIAAxkDAAMpZtro7cUlU_0taPfUxIg9cQM6n8oAAsPiMRvMb9hKJkkcOZWgqRUBAAMCAAN5AAM2BA'
    text = await get_str_from_txt(Path('src', 'data', 'messages', 'menu_message', 'menu_text.txt'))
    media = InputMediaPhoto(media=photo, caption=text)
    keyboard = start_menu_keyboard
    await message.edit_media(media=media, reply_markup=keyboard)


