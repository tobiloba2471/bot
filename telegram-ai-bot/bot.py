from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8031390637:AAEm7I33EttH7T1aB33FudiOf9iQpN-STOk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your AI Bot.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
