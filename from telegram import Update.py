from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# أدخل الـ Token الخاص بك هنا
TOKEN = "7021270661:AAHZFg_Mj0j-ZgoJVUbGkdhuHQHV55F1nYM"

# دالة الرد على الأمر /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("مرحبًا! أنا بوت الردود التلقائية. أرسل لي كلمة وسأرد عليك.")

# دالة الرد التلقائي
def auto_reply(update: Update, context: CallbackContext):
    # قائمة الردود التلقائية
    responses = {
        "مرحبًا": "أهلًا وسهلًا! 😊",
        "كيف حالك؟": "أنا بوت، لا أشعر، لكن شكراً للسؤال! 🤖",
        "وداعًا": "إلى اللقاء! 👋"
    }

    # الحصول على نص الرسالة
    user_message = update.message.text

    # الرد إذا كانت الكلمة موجودة في القائمة
    reply = responses.get(user_message, "عذرًا، لا أفهم ما تقول.")

    update.message.reply_text(reply)

# إعداد البوت
def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # ربط الأوامر والدوال
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, auto_reply))

    # بدء تشغيل البوت
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
