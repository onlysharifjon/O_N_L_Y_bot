# from cgitb import text
import types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiohttp import request
# from sqlalchemy import true
# from telegram import Contact
startbut = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Buyurtma berish"),
        ],
        [
            KeyboardButton(text = "Admin bilan Bog`lanish"),
        ],
        
    ],
    resize_keyboard=True,
)