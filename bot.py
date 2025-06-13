# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# BOT_TOKEN = "7536909803:AAHG6BGLWW4JFiBboGOxfb0C2dC3RB-f72o"
# CHANNEL_USERNAME = "@Nasiba_EmpowerU"
# PRIVATE_GROUP_LINK = "https://t.me/+Q2g12YUoNhRmNjMy"

# users = {}

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id
#     args = context.args

#     if user_id not in users:
#         users[user_id] = {"referred_by": None, "invited": [], "subscribed": False}

#     if args:
#         try:
#             ref_id = int(args[0])
#             if ref_id != user_id:
#                 users[user_id]["referred_by"] = ref_id
#         except ValueError:
#             pass
#     await context.bot.send_photo(
#         chat_id=update.effective_chat.id,
#         photo=open("static/nasiba.jpg", "rb"),
#         caption=f"""‼️ Diqqat bilan o‘qing 👇

# 🗣️ 15 kun davomida ingliz tilida bemalol, ishonch bilan gapirishni o‘rganmoqchimisiz? Unda ushbu 100% BEPUL “Fluent in 15” onlayn kursi aynan siz uchun!

# ✨ Bu kurs orqali siz:
# ✅ Har kuni yangicha speaking mavzularida gapirasiz  
# ✅ So‘z boyligingizni oshirasiz  
# ✅ Grammar + real speaking mashqlarni birgalikda o‘rganasiz  
# ✅ Har bir darsdan so‘ng PDF materiallarni olasiz 
# ✅ Shaxsiy yopiq guruhda qatnashasiz  
# ✅ 15 kun davomida ingliz tilida gapirishga odatlanasiz  

# 📌 Kurs 15 kun davom etadi. Har kuni yangi dars!  
# 📩 Darslar onlayn formatda bo‘lib o‘tadi."""
#             )

#     keyboard = InlineKeyboardMarkup([
#         [InlineKeyboardButton("🔗 Kanalga obuna bo‘lish", url=f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}")],
#         [InlineKeyboardButton("✅ Obuna bo‘ldim", callback_data="check_sub")]
#     ])

#     await context.bot.send_message(
#         chat_id=update.effective_chat.id,
#         text="👇 Quyidagi tugmani bosib kanalga obuna bo‘ling va keyin 'Obuna bo‘ldim' tugmasini bosing.",
#         reply_markup=keyboard
#     )


# async def check_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
#     user_id = query.from_user.id

#     try:
#         member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
#     except Exception as e:
#         await query.edit_message_text("❌ Obunani tekshirishda xatolik yuz berdi.")
#         return

#     if member.status in ["member", "administrator", "creator"]:
#         users[user_id]["subscribed"] = True
#         await query.edit_message_text("✅ Obuna tasdiqlandi!")
#         referrer = users[user_id].get("referred_by")
#         if referrer and referrer in users:
#             if user_id not in users[referrer]["invited"]:
#                 users[referrer]["invited"].append(user_id)
#                 if len(users[referrer]["invited"]) >= 3:
#                     await context.bot.send_message(
#                         chat_id=referrer,
#                         text=f"🎉 Sizga 3 do‘stingiz obuna bo‘ldi!\n🔐 Yopiq guruh: {PRIVATE_GROUP_LINK}"
#                     )

#         bot_user = await context.bot.get_me()
#         ref_link = f"https://t.me/{bot_user.username}?start={user_id}"
#         await context.bot.send_message(
#             chat_id=user_id,
#             text=f"🎯 Referal link: {ref_link}\n👤 Qo‘shilish shartlari 🎯 📲 Kursga yozilish uchun faqatgina 3 nafar do‘stingizni kanalga taklif qilasiz. Ular kanalga qo‘shilgach, sizga avtomatik ravishda kurs havolasi yuboriladi!"
#         )
#     else:
#         keyboard = InlineKeyboardMarkup([
#             [InlineKeyboardButton("🔗 Kanalga obuna bo‘lish", url=f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}")],
#             [InlineKeyboardButton("✅ Obuna bo‘ldim", callback_data="check_sub")]
#         ])
#         await query.edit_message_text(
#             text="❌ Siz hali obuna bo‘lmagansiz. Iltimos, kanalga obuna bo‘ling va keyin 'Obuna bo‘ldim' tugmasini bosing.",
#             reply_markup=keyboard
#         )




# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id

#     if users.get(user_id, {}).get("referred_by") and users.get(user_id).get("subscribed"):
#         referrer = users[user_id]["referred_by"]

#         if referrer in users and user_id not in users[referrer]["invited"]:
#             users[referrer]["invited"].append(user_id)

#             if len(users[referrer]["invited"]) >= 3:
#                 await context.bot.send_message(
#                     chat_id=referrer,
#                     text=f"🎉 Do‘stingiz obuna bo‘ldi!\n🔐 Yopiq guruh: {PRIVATE_GROUP_LINK}"
#                 )

# if __name__ == "__main__":
#     app = ApplicationBuilder().token(BOT_TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CallbackQueryHandler(check_subscription, pattern="check_sub"))
#     app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
#     app.run_polling()



from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7536909803:AAFtHrz34BgZKfpGqtjDj3_JDjK0Gh2xD_w"
CHANNEL_USERNAME = "@Nasiba_EmpowerU"
PRIVATE_GROUP_LINK = "https://t.me/+Q2g12YUoNhRmNjMy"

# Foydalanuvchilar ma'lumotlarini saqlash (keyinchalik DBga o‘zgartirish mumkin)
users = {}

def get_subscription_keyboard():
    """Kanalga obuna bo‘lish uchun inline klaviatura"""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔗 Kanalga obuna bo‘lish", url=f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}")],
        [InlineKeyboardButton("✅ Obuna bo‘ldim", callback_data="check_sub")]
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    args = context.args

    if user_id not in users:
        users[user_id] = {"referred_by": None, "invited": [], "subscribed": False}

    if args:
        try:
            ref_id = int(args[0])
            if ref_id != user_id:
                users[user_id]["referred_by"] = ref_id
        except ValueError:
            pass

    with open("static/nasiba.jpg", "rb") as photo_file:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photo_file,
            caption=(
            "‼️ Diqqat bilan o‘qing 👇\n\n"
            "🗣️ 15 kun davomida ingliz tilida bemalol, ishonch bilan gapirishni o‘rganmoqchimisiz? "
            "Unda ushbu 100% BEPUL “Fluent in 15” onlayn kursi aynan siz uchun!\n\n"
            "✨ Bu kurs orqali siz:\n"
            "✅ Har kuni yangicha speaking mavzularida gapirasiz\n"
            "✅ So‘z boyligingizni oshirasiz\n"
            "✅ Grammar + real speaking mashqlarni birgalikda o‘rganasiz\n"
            "✅ Har bir darsdan so‘ng PDF materiallarni olasiz\n"
            "✅ Shaxsiy yopiq guruhda qatnashasiz\n"
            "✅ 15 kun davomida ingliz tilida gapirishga odatlanasiz\n\n"
            "📌 Kurs 15 kun davom etadi. Har kuni yangi dars!\n"
            "📩 Darslar onlayn formatda bo‘lib o‘tadi."
            )
        )

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="👇 Quyidagi tugmani bosib kanalga obuna bo‘ling va keyin 'Obuna bo‘ldim' tugmasini bosing.",
        reply_markup=get_subscription_keyboard()
    )

async def check_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
    except Exception:
        await query.edit_message_text("❌ Obunani tekshirishda xatolik yuz berdi. Iltimos, keyinroq qayta urinib ko‘ring.")
        return

    if member.status in ["member", "administrator", "creator"]:
        users[user_id]["subscribed"] = True
        await query.edit_message_text("✅ Obuna tasdiqlandi!")

        referrer = users[user_id].get("referred_by")
        if referrer and referrer in users:
            if user_id not in users[referrer]["invited"]:
                users[referrer]["invited"].append(user_id)
                if len(users[referrer]["invited"]) >= 3:
                    await context.bot.send_message(
                        chat_id=referrer,
                        text=(
                            "🎉 Sizga 3 do‘stingiz obuna bo‘ldi!\n"
                            f"🔐 Yopiq guruhga kirish uchun havola: {PRIVATE_GROUP_LINK}"
                        )
                    )

        bot_user = await context.bot.get_me()
        ref_link = f"https://t.me/{bot_user.username}?start={user_id}"
        await context.bot.send_message(
            chat_id=user_id,
            text=(
                f"🎯 Referal link: {ref_link}\n\n"
                "👤 Qo‘shilish shartlari:\n"
                "📲 Kursga yozilish uchun faqatgina 3 nafar do‘stingizni kanalga taklif qilasiz. "
                "Ular kanalga qo‘shilgach, sizga avtomatik ravishda kurs havolasi yuboriladi!"
            )
        )
    else:
        await query.edit_message_text(
            text="❌ Siz hali obuna bo‘lmagansiz. Iltimos, kanalga obuna bo‘ling va keyin 'Obuna bo‘ldim' tugmasini bosing.",
            reply_markup=get_subscription_keyboard()
        )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_data = users.get(user_id)
    if not user_data:
        return

    if user_data.get("subscribed") and user_data.get("referred_by"):
        referrer = user_data["referred_by"]

        if referrer in users and user_id not in users[referrer]["invited"]:
            users[referrer]["invited"].append(user_id)

            if len(users[referrer]["invited"]) >= 3:
                await context.bot.send_message(
                    chat_id=referrer,
                    text=(
                        "🎉 Do‘stingiz obuna bo‘ldi!\n"
                        f"🔐 Yopiq guruhga kirish uchun havola: {PRIVATE_GROUP_LINK}"
                    )
                )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_subscription, pattern="check_sub"))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Bot ishga tushdi...")
    app.run_polling()
