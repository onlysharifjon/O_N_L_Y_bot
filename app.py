import logging
from aiogram.types import CallbackQuery

from db import insert_or_update
from keyboards.default.startkey import startbut
from keyboards.inline.avtor import FOLLOWER_INSTA, LIKES_INSTA, WIEW_INSTAGRAM, PAY_URL
from keyboards.default.socials import contact, startnak, menu_nak, KEYBOARD_PAY
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6014525433:AAGcROIah3eHIFssNtBObNr0QBJUiYEF85g'

logging.basicConfig(level=logging.INFO)
ADMINS = 5172746353
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        f"Assalomu Aleykum Hurmatli,<b> {message.from_user.full_name}</b>!\nSiz botimizning Yangi foydalanuvchisi siz\nsiz uchun maxsus <b>🎁BONUS🎁 </b>lar mavjud",
        reply_markup=startbut)


@dp.message_handler(text="Buyurtma berish")
async def sharif(message: types.Message):
    await message.answer(f"Nakrutka xizmatidan foydalanish uchun <b>Kontakt</b> yuboring", reply_markup=contact)


@dp.message_handler(content_types="contact")
async def sharif(message: types.Message):
    full_name = message.contact.full_name
    username = message.chat.username
    phone_number = message.contact.phone_number
    user_id = message.contact.user_id
    # is_updated = insert_or_update(full_name, username, phone_number, user_id)
    is_updated = True
    await bot.send_message(ADMINS, message.contact)
    if is_updated:
        await message.answer(f"Kontakt qabul qilindi\n<b>XUSH KELIBSIZ</b>{message.from_user.full_name}", reply_markup=startnak)
    else:
        await message.answer("Qo'shildi", reply_markup=startnak)

@dp.message_handler(text="Admin bilan Bog`lanish")
async def show_menu(message: types.Message):
    await message.answer(f"⬇️Admin akkauntlari ro`yxati⬇️\n👮‍♂️@notify33\n👮‍♂️@shar1fjon\n👮‍♂️@OpenWiki")




@dp.message_handler(text="🕸 Instagram 🕸")
async def show_nakrutka(message: types.Message):
    await message.answer("Instagram Nakrutka Bo`limidasiz", reply_markup=menu_nak)


followers = 0
likes = 0
wiews = 0


@dp.message_handler(text="Obunachilar🫂")
async def show_instagram(message: types.Message):

    followers = 0
    await message.answer("<b>Instagramdagi Obunachilar sonini tanlang👤</b>")
    await message.answer(f"Instagram 👤obunachilar👤 soni: <b>{followers}</b>", reply_markup=FOLLOWER_INSTA)


@dp.callback_query_handler(text="ayrish")
async def qoshish(call: CallbackQuery):
    global followers
    followers -= 1000
    await call.message.edit_text(f"Instagram 👤obunachilar👤 soni: <b>{followers}</b>", reply_markup=FOLLOWER_INSTA)
    await call.answer("-1000")


@dp.callback_query_handler(text="qoshish")
async def ayrish(call: CallbackQuery):
    global followers
    followers += 1000
    await call.message.edit_text(f"Instagram 👤obunachilar👤 soni: <b>{followers}</b>", reply_markup=FOLLOWER_INSTA)
    await call.answer("+1000")


@dp.callback_query_handler(text="Tasdiqlash")
async def tasdiqlash(call: CallbackQuery):
    global followers
    natija = followers * 10
    await call.message.delete()
    followers = 0
    await call.message.answer(f"Buyurtma narxi: <b>{natija}USZ</b>", reply_markup=KEYBOARD_PAY)
    await call.answer("Narx")


########################################################

@dp.message_handler(text="Like❤️")
async def show_instagram(message: types.Message):
    likes = 0
    await message.answer("<b>Instagramdagi Postingiz like(❤) sonini tanlang</b>")
    await message.answer(f"Instagram Likelar❤  soni: <b>{likes}</b>", reply_markup=LIKES_INSTA)


@dp.callback_query_handler(text="Ayrish_like")
async def qoshish(call: CallbackQuery):
    global likes
    likes -= 1000
    await call.message.edit_text(f"Instagram Likelar❤️ soni: <b>{likes}</b>", reply_markup=LIKES_INSTA)
    await call.answer("-1000")


@dp.callback_query_handler(text="qoshish_like")
async def ayrish(call: CallbackQuery):
    global likes
    likes += 1000
    await call.message.edit_text(f"Instagram Likelar❤️ soni: <b>{likes}</b>", reply_markup=LIKES_INSTA)
    await call.answer("+1000")


@dp.callback_query_handler(text="Tasdiqlash_like")
async def tasdiqlash(call: CallbackQuery):
    global likes
    natija_like = likes * 3
    await call.message.delete()
    likes = 0
    await call.message.answer(f"Buyurtma narxi: <b>{natija_like}USZ</b>", reply_markup=KEYBOARD_PAY)
    await call.answer("Narx")


######################################################

@dp.message_handler(text="Prasmotrlar👁👁")
async def show_instagram(message: types.Message):
    wiews = 0
    await message.answer("<b>Instagramdagi Postingiz Prasmotrlar👁👁 sonini tanlang</b>")
    await message.answer(f"Instagram Prasmotrlar👁👁  soni: <b>{wiews}</b>", reply_markup=WIEW_INSTAGRAM)


@dp.callback_query_handler(text="Ayrish_wiew")
async def qoshish(call: CallbackQuery):
    global wiews
    if wiews >= 1000:
        wiews -= 1000
        await call.message.edit_text(f"Instagram Prasmotrlar👁👁 soni: <b>{wiews}/b>", reply_markup=WIEW_INSTAGRAM)
        await call.answer("-1000")
    else:
        await call.answer(text="Minimal buyurtma 1000", show_alert=True)


@dp.callback_query_handler(text="qoshish_wiev")
async def ayrish(call: CallbackQuery):
    global wiews
    wiews += 1000
    await call.message.edit_text(f"Instagram Prasmotrlar👁👁 soni:<b>{wiews}</b>", reply_markup=WIEW_INSTAGRAM)


@dp.callback_query_handler(text="Tasdiqlash_wiev")
async def tasdiqlash(call: CallbackQuery):
    global wiews
    natija_wiew = wiews * 2
    wiews = 0
    await call.message.delete()
    await call.message.answer(f"Buyurtma narxi: {natija_wiew}USZ", reply_markup=KEYBOARD_PAY)
    await call.answer("Narx")


@dp.message_handler(text="TO`LASH✅")
async def pay(message: types.Message):
    # studyboi = InlineKeyboardButton('Admin orqali to`lash', url='https://t.me/shar1fjon')
    # start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(studyboi)
    await message.answer(
        '💳<b>UZCARD:</b> <code>8600312910441829</code>\n💳ADMIN ORQALI TO`LOVINGIZNI TASDIQLANG',
        reply_markup=PAY_URL)
    await message.answer(
        "🟡Boshqa buyurtma berishingi uchun menu yangilandi\n🟡Joriy buyurtmangiz Admin to`lov tizimi orqali bajariladi",
        reply_markup=menu_nak)


@dp.message_handler(text="QAYTISH❌")
async def pay(message: types.Message):
    await  message.answer("❌Buyurtma bekor qilinidi❌", reply_markup=menu_nak)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
