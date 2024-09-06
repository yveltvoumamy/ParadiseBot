from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

buy_ticket_buttons = [
    [
        InlineKeyboardButton(text='Один билет', callback_data='one_ticket'),
        InlineKeyboardButton(text='Два билета', callback_data='two_ticket')
    ],
    [
        InlineKeyboardButton(text='Вернуться в главное меню', callback_data='menu')
    ]
]

cancel_button = [
    [InlineKeyboardButton(text='Отменить покупку', callback_data='cancel_buy')]
]

buy_ticket_keyboard = InlineKeyboardMarkup(inline_keyboard=buy_ticket_buttons)
cancel_keyboard = InlineKeyboardMarkup(inline_keyboard=cancel_button)