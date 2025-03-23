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
    await message.answer("Assalomu alaykum! Ushbu bot O'ktamova Sarvinozxon tomonidan G‘afur G‘ulom xotirasini abadiylashtirish va ijodini targ'ib qilish maqsadida yaratildi.", reply_markup=keyboard)

@dp.message(lambda message: message.text == "Hayoti va ijodi")
async def send_biography(message: types.Message):
    text = (
        '''📖 G‘afur G‘ulom — O‘zbekistonning taniqli yozuvchisi. Urushdan keyingi davrdagi o‘zbek adabiyoti rivojida beqiyos o‘rin tutgan shaxs.
G‘afur G‘ulom 1903-yilning 10-may kuni Toshkentda, dehqonlar oilasida tug‘ilgan. Uning otasi savodxon bo‘lgan. U o‘zbek va tojik mumtoz adabiyotini o‘qigan, rus tilini bilgan, o‘zi ham she’rlar yozgan. Uning uyiga Muqimiy, Furqat, Asiriy, Xislat va boshqa shoirlar kelib turgan.
1916 yilning kuzida G‘afur o‘qishga kiradi. Ota-onasining vafotidan so‘ng u ishlashga majbur bo‘lgan. Ko‘plab kasblarda o‘zini sinab ko‘rgach, u nihoyat, matbaaga harf teruvchi bo‘lib ishga kiradi, so‘ngra, pedagogik kurslarda tahsil oladi. 1919-yildan 1927-yilgacha u o‘qituvchi, maktab direktori, Ma’naviyat uyushmasi ishchilari raisi bo‘lib ishlaydi, bolalar uyini tashkil etishda faol ishtirok etadi.

Adabiyotdagi faoliyati
1923 yildan G‘afur G‘ulomning adabiy faoliyati boshlanadi. She’rlar, dostonlar, ocherklar, hajviy hikoyalar va qissalari gazeta va jurnallarda chop etila boshlaydi. 1923-yil yozilgan “Feliks farzandlari” she’rida yetim bolalar haqida gapirarkan, unda yozuvchi o‘z hayotini ifodalaydi, “Maorif va o‘qituvchi” oynomasida esa “Go‘zallik qayerda” nomli ikkinchi she’ri nashr qilinadi. Birin-ketin she’riy to‘plamlari bosmadan chiqadi: “Dinamo”, “Xitoy suratlari”, “Biz sizlar bilan tirikmiz”, “Jonli qo‘shiqlar”, “Sizga”, “Sovg‘a”, “Tong qo‘shig‘i”, “Qo‘qon” dostoni va boshqalar.
G‘afur G‘ulomning 30-yil boshlarida yozilgan she’rlarida yangi shakllarga burilish seziladi, bunga mumtoz rus tilini o‘rganishi ham muhim darajada ta’sir ko‘rsatgan. Bundan tashqari, sanoatning o‘sishi, Turksib temir yo‘l magistralining qurilishi kabi uning ona yurtida sodir bo‘layotgan ajoyib o‘zgarishlarni ta’riflash uchun yangi lug‘at boyligi, yangi she’riy bo‘yoqlar, yangi ohang va vazn talab etilgan.
“Dinamo” (1931), “Tirik qo‘shiqlar” (1932) — yosh shoirning yo‘nalishi yorqin namoyon bo‘lgan birinchi she’riy to‘plamlari.
Shoirning boqiy hayot, mangu ko‘k daraxt haqidagi “Qish va qor” (1929), “Non” (1931), “Toshkent” (1933), “Qutbda saylovlar” (1937), “Men - Yahudiyman” (1941), “Qish” (1941), “Xotin” (1942), “Afsuski, afsusni qo‘shib ko‘mmadi” (1945), “Bog‘” (1934), “Qayg‘u” (1942), “Kuz keldi” (1945), “Kuzgi ko‘chatlar” (1948) kabi she’rlarida umuminsoniylik, insonparvarlik mavzulari o‘z aksini topdi.
Ko‘pgina she’rlarida sharq donishmandi – ota timsoli mavjud: “Sen yetim emassan” (1942), “Qayg‘u” (1942), “Biri biriga shogird, biri biriga ustod” (1950), “Sizlarga - yoshlar” (1947), “Bahor taronalari” (1948) va boshqalar.
“Netay” (1930), “Yodgor” (1936), “Shum bola” (1936-1962) qissalari va “Shariat nayranglari” (1930), “Mening o‘g‘rigina bolam” (1965) hikoyalarida chinakam xalq qahramonlari, milliyligimiz tavsirlangan.
O‘zbekiston Fanlar akademiyasi akademiki G‘afur G‘ulom “Navoiy va bizning davr” (1948), “Folklordan o‘rganaylik” (1939) tadqiqotlarini, “Jaloliddin dramasi haqida” (1945), “Muqimiy” (1941) maqolalarini yaratgan.
G‘afur G‘ulom qisqa, o‘tkir sujetli hikoyalar ustasi sifatida ham taniqli bo‘lib, hikoya uslubi o‘rnida u yozuvchining savol-javoblari bilan to‘ldirilgan jonli do‘stona bahs-munozara shaklida, mualliflik nutqi va kitobxonga erkin yuzlanish orqali foydalanadi. G‘afur G‘ulom tomonidan 30-yillarda yaratilgan ko‘plab nasriy asarlar yangi insoniy munosabatlarga bag‘ishlangan. U asarlarida yoritgan asosiy muammo va yechimlar – bu insonning axloqiy tarbiyasi, uning ma’naviy va madaniy rivoji sari kurashdir.

G‘afur G‘ulom ko‘plab asarlarini bolalarga bag‘ishlagan. “Shum bola” hikoyasi boshqalariga qaraganda anchagina omadli hisoblanadi.
Shuningdek, yozuvchi bolalar va o‘smirlarga bag‘ishlab, “Ikki bolalik”, “Bilaman”, “Seni Vatan kutmoqda” kabi she’rlarni yozgan.'''
    )
    await message.answer(text)

@dp.message(lambda message: message.text == "Suratlar")
async def send_photos(message: types.Message):
    photo_urls = [
        "https://upload.wikimedia.org/wikipedia/commons/3/30/%D0%93%D0%B0%D1%84%D1%83%D1%80_%D0%93%D1%83%D0%BB%D1%8F%D0%BC_%28%D0%BF%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82%29.jpg",
        "https://yuz.uz/file/news/dc3011b919da5b4b731e955c6180e6a1.jpg",
        "https://cdn1.img.sputniknews.uz/img/07e7/04/0b/33787405_0:12:543:419_1920x0_80_0_0_ac9a683f2b842b71e6d7ca509db28f5c.jpg",
        "https://tashkenttimes.uz/images/Personalities/Gafur-gulam.jpg"

    ]
    for url in photo_urls:
        await message.answer_photo(url)

@dp.message(lambda message: message.text == "Asarlar")
async def forward_post(message: types.Message):
    from_chat_id = -1002645353989  # 📢 Kanal yoki guruh ID'sini shu yerga yozing
    message_id = 2  # 📝 Forward qilmoqchi bo'lgan post ID'si

    await bot.copy_message(chat_id=message.chat.id, from_chat_id=from_chat_id, message_id=message_id)
# async def send_pdf(message: types.Message):
#     pdf_urls = [
#         "https://ipkmvd.uz/media/pdf/kitoblar/Shum_bola_Gafur_Gulom.pdf",
#     ]  # 📂 Shu yerga PDF URL'larni kiriting
#
#     for url in pdf_urls:
#         await message.answer_document(url)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)  # Eski xabarlarni tozalash
    await dp.start_polling(bot)  # Botni ishga tushirish

if __name__ == "__main__":
    asyncio.run(main())