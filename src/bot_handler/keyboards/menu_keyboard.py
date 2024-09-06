from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

start_menu_buttons = [
    [InlineKeyboardButton(text='Купить билет', callback_data='tiket_buy')],
    [InlineKeyboardButton(text='Текущее мероприятие', callback_data='current_party')],
    [InlineKeyboardButton(text='Прерыдущие мероприятия', callback_data='previous_party')],
    [InlineKeyboardButton(text='Отзывы', callback_data='feedback')],
    [InlineKeyboardButton(text='Участвовать в конкурсе', callback_data='contest')],
    [InlineKeyboardButton(text='Связаться с менеджером', callback_data='contact', url='https://t.me/yaneshizik')]

]

next_step_menu_button = [
    [InlineKeyboardButton(text='darow', callback_data='darow_back')]
]

start_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=start_menu_buttons)
next_step_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=next_step_menu_button)