# 🤖 TelegramBot OOP

Bot Telegram scritto in Python, con una struttura modulare basata sulla **programmazione a oggetti (OOP)**. Facile da estendere, sicuro da configurare, perfetto come base per progetti bot avanzati.

---

## 🚀 Funzionalità

- Comandi `/start` e `/help`
- Architettura OOP: comandi separati in una classe
- Token gestito da file `config.json`
- Costruito con la libreria `python-telegram-bot` (v20+)
- Facile da estendere con nuovi comandi o logica

---

## 🗂️ Struttura del progetto
```
telegram_bot_oop/
├── main.py # Entrypoint principale del bot
├── commands.py # Classe con i comandi del bot
├── config.json # Contiene in modo sicuro il token
```


---

## ⚙️ Requisiti

- Python 3.9+
- `python-telegram-bot` v20 o superiore

Installa le dipendenze:

```bash
pip install python-telegram-bot --upgrade
```

🧪 Esecuzione

1. Crea un bot con BotFather e copia il token.
2. Inserisci il token nel file config.json:
3. 
```
{
  "token": "INSERISCI_IL_TUO_TOKEN_QUI"
}
```
3. Avvia il bot:
```
python main.py
```
