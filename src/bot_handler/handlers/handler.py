from aiogram import F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from src.bot_handler.bot import bot, dp
from src.bot_handler.keyboards.menu_keyboard import start_menu_keyboard, next_step_menu_keyboard

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
    await message.answer(text='дароу', reply_markup=start_menu_keyboard)
1

@dp.callback_query(F.data == 'darow')
async def process_darow(callback_query: CallbackQuery) -> None:
    await callback_query.answer(f'')
    message = callback_query.message
    await bot.edit_message_text(text='darow', chat_id=message.chat.id, message_id=message.message_id)
    await bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message.message_id,
                                        reply_markup=next_step_menu_keyboard)


@dp.callback_query(F.data == 'darow_back')
async def process_darow_back(callback_query: CallbackQuery) -> None:
    await callback_query.answer(f'')
    message = callback_query.message
    await bot.edit_message_text('дароу', chat_id=message.chat.id, message_id=message.message_id)
    await bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message.message_id,
                                        reply_markup=start_menu_keyboard)