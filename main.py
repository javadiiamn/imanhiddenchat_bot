from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8319558566:AAETQWbvE4ZaSM13_v5vPOAxxc-yv-VZNZI"
ADMIN_ID = 6810586753

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام
میتونی هر پیامی داری برای ایمان بنویسی و من ناشناس براش ارسال کنم.")

async def forward_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"پیام جدید:\n\n{message}"
    )
    await update.message.reply_text("مرسی! پیامت ثبت شد ✅")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_feedback))
    app.run_polling()

if name == "main":
    main()
