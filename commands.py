from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

class Commands:

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update._effective_chat.id, text="Benevuto il bot è stato avviato correttamente")

    def get_commands(self):
        return [
            CommandHandler("start", self.start),
        ]