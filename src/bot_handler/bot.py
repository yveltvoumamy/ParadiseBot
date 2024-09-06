from aiogram import Bot, Dispatcher
from src.data.file_manager import get_attr_from_csv

bot = Bot(get_attr_from_csv('config', 'token'))
dp = Dispatcher()