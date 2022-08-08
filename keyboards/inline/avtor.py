from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

FOLLOWER_INSTA = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="🤳-1000🤳", callback_data="ayrish"),
            InlineKeyboardButton(text="🤳Tasdiqlash🤳", callback_data="Tasdiqlash"),
            InlineKeyboardButton(text="🤳+1000🤳", callback_data="qoshish"),            
        ],
    ],
)
LIKES_INSTA= InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="🤳-1000🤳", callback_data="Ayrish_like"),
            InlineKeyboardButton(text="🤳Tasdiqlash🤳", callback_data="Tasdiqlash_like"),
            InlineKeyboardButton(text="🤳+1000🤳", callback_data="qoshish_like"),
            
            
        ],

    ],  
)

WIEW_INSTAGRAM= InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="🤳-1000🤳", callback_data="Ayrish_wiew"),
            InlineKeyboardButton(text="🤳Tasdiqlash🤳", callback_data="Tasdiqlash_wiev"),
            InlineKeyboardButton(text="🤳+1000🤳", callback_data="qoshish_wiev"),  
        ],
    ],  
)
PAY_URL= InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="ADMIN",url="https://t.me/shar1fjon"),
        ],
    ],
)
