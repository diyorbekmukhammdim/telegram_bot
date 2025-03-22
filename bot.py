from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

TOKEN = "8184836337:AAHH9pyRAj9vfEsK3u9S5YymZNz_acRQsoE"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Tugmalarni yaratamiz
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton("Hayoti va ijodi")
btn2 = KeyboardButton("Suratlar")
keyboard.add(btn1, btn2)


# Start komandasi
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Assalomu alaykum! Men G‘afur G‘ulom botiman.", reply_markup=keyboard)


# "Hayoti va ijodi" tugmasi bosilganda
@dp.message_handler(lambda message: message.text == "Hayoti va ijodi")
async def send_biography(message: types.Message):
    text = (
        "📖 G‘afur G‘ulom (1903-1966) - O‘zbek adabiyotining yirik vakillaridan biri, "
        "shoir va yozuvchi. Uning mashhur asarlari orasida 'Shum bola', 'Netay' "
        "kabi asarlar bor. Uning ijodi adabiy tanqidchilar tomonidan yuksak baholangan."
    )
    await message.answer(text)


# "Suratlar" tugmasi bosilganda
@dp.message_handler(lambda message: message.text == "Suratlar")
async def send_photos(message: types.Message):
    photo_urls = [
        "https://upload.wikimedia.org/wikipedia/commons/3/30/%D0%93%D0%B0%D1%84%D1%83%D1%80_%D0%93%D1%83%D0%BB%D1%8F%D0%BC_%28%D0%BF%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82%29.jpg"
    ]

    for url in photo_urls:
        await message.answer_photo(url)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
