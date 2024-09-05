from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

start_menu_buttons = [
    [InlineKeyboardButton(text='Дароу', callback_data='darow')]
]

next_step_menu_button = [
    [InlineKeyboardButton(text='darow', callback_data='darow_back')]
]

start_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=start_menu_buttons)
next_step_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=next_step_menu_button)