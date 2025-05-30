import json
from telegram.ext import ApplicationBuilder
from commands import Commands

class Main:
    def __init__(self, config_path="config.json"):
        self.token = self._get_token(config_path)
        self.commands = Commands()

    def _get_token(self, path):
        with open(path, 'r') as f:
            config = json.load(f)
            token = config.get("token")
            return token

    def run(self):
        app = ApplicationBuilder().token(token=self.token).build()
        commands = self.commands.get_commands()

        for command in commands:
            app.add_handler(command)

        print("🤖 Bot in esecuzione...")
        app.run_polling()

if __name__ == "__main__":
    bot = Main()
    bot.run()