import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

TOKEN = "8184836337:AAHH9pyRAj9vfEsK3u9S5YymZNz_acRQsoE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Tugmalarni to‘g‘ri formatda yaratish
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Hayoti va ijodi")],
        [KeyboardButton(text="Suratlar")],
        [KeyboardButton(text="Asarlar")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Assalomu alaykum! Men G‘afur G‘ulom botiman.", reply_markup=keyboard)

@dp.message(lambda message: message.text == "Hayoti va ijodi")
async def send_biography(message: types.Message):
    text = (
        "📖 G‘afur G‘ulom (1903-1966) - O‘zbek adabiyotining yirik vakillaridan biri. "
        "Uning mashhur asarlari orasida 'Shum bola', 'Netay' kabi asarlar bor."
    )
    await message.answer(text)

@dp.message(lambda message: message.text == "Suratlar")
async def send_photos(message: types.Message):
    photo_urls = [
        "https://upload.wikimedia.org/wikipedia/commons/3/30/%D0%93%D0%B0%D1%84%D1%83%D1%80_%D0%93%D1%83%D0%BB%D1%8F%D0%BC_%28%D0%BF%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82%29.jpg"
    ]
    for url in photo_urls:
        await message.answer_photo(url)

@dp.message(lambda message: message.text == "Asarlar")
async def send_pdf(message: types.Message):
    pdf_urls = [
        "https://ipkmvd.uz/media/pdf/kitoblar/Shum_bola_Gafur_Gulom.pdf",
    ]  # 📂 Shu yerga PDF URL'larni kiriting

    for url in pdf_urls:
        await message.answer_document(url)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)  # Eski xabarlarni tozalash
    await dp.start_polling(bot)  # Botni ishga tushirish

if __name__ == "__main__":
    asyncio.run(main())