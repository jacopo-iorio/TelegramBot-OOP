import json
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

class Commands:

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat = update._effective_chat.id
        msg = self._get_message().get("start")
        await context.bot.send_message(chat_id=chat, text=msg)

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat = update._effective_chat.id
        msg = self._get_message().get("help")
        await context.bot.send_message(chat_id=chat, text=msg, parse_mode="Markdown")

    def _get_message(self, path="message.json"):
        with open(path, "r", encoding="utf-8") as f:
            message = json.load(f)
            return message

    def get_commands(self):
        return [
            CommandHandler("start", self.start),
            CommandHandler("help", self.help),
        ]