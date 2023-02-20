# from cgitb import text
import types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

from aiohttp import request
# from sqlalchemy import true
# from telegram import Contact
startnak = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "🕸 Instagram 🕸"),
          
        ],
        
    ],
    resize_keyboard=True,
)
menu_nak = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Obunachilar🫂"),
          
        ],
        [
            KeyboardButton(text = "Like❤️"),
          
        ],
         [
            KeyboardButton(text = "Prasmotrlar👁👁"),
          
        ],
        
    ],
    resize_keyboard=True,
)



contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text= "Kontakt yuboring📞",request_contact=True)
        ],
    ],
    resize_keyboard=True,
)
KEYBOARD_PAY= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text= "TO`LASH✅")
        ],
        [
            KeyboardButton(text= "QAYTISH❌")
        ],
    ],
    resize_keyboard=True,
)