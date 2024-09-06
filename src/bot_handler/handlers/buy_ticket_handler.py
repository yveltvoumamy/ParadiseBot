from aiogram import F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, FSInputFile, InputMediaPhoto
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

import os
from pathlib import Path

from src.bot_handler.bot import bot, dp
from src.bot_handler.keyboards.buy_ticket_keyboards import buy_ticket_keyboard, cancel_keyboard
from src.data.file_manager import get_str_from_txt

@dp.callback_query(F.data == 'tiket_buy')
async def process_ticket_buy(callback_query: CallbackQuery) -> None:
    await callback_query.answer(f'')
    message = callback_query.message
    photo = FSInputFile(Path('src', 'data', 'messages', 'buy_ticket_message', 'ticket_photo.png'))
    text = await get_str_from_txt(Path('src', 'data', 'messages', 'buy_ticket_message', 'buy_ticket_message.txt'))
    keyboard = buy_ticket_keyboard
    # await message.answer_photo(photo=photo)
    media = InputMediaPhoto(media='AgACAgIAAxkDAAMuZtr8B_A3rZN1NcnxFjmmxRQJBMQAAlHjMRvMb9hK5ZJ8gWYLcJsBAAMCAAN3AAM2BA',
                            caption=text)
    await message.edit_media(media=media, reply_markup=keyboard)
