# 📍 Flask Real-Time GPS Tracker

A simple and lightweight real-time location tracking system built with Python (Flask) and JavaScript. This tool captures GPS coordinates, IP addresses, and device information, then sends them directly to a Telegram bot.

## 🚀 Features
- **Real-time GPS Tracking:** Captures Latitude and Longitude with high accuracy.
- **Device Info:** Logs the user's IP address and Browser/OS details (User-Agent).
- **Telegram Integration:** Instant notifications sent directly to your Telegram chat.
- **Auto-Redirect:** Automatically redirects the target user to a specific YouTube video or any URL to avoid suspicion.

## 🛠️ Tech Stack
- **Backend:** Python (Flask)
- **Frontend:** HTML5, CSS3, JavaScript (Geolocation API)
- **Notifications:** Telegram Bot API
- **Deployment:** Koyeb / Render / PythonAnywhere

## 📋 Prerequisites
Before running the project, ensure you have:
- Python 3.x installed.
- A Telegram Bot Token (from [@BotFather](https://t.me/botfather)).
- Your Telegram Chat ID (from [@userinfobot](https://t.me/userinfobot)).

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

2. **Configurate the bot**
   ```bash
   BOT_TOKEN = "your_bot_token_here"
   CHAT_ID = "your_chat_id_here"
3. **Run the application**
   ```bash
   python app.py

 ## 🌐 Deployment

To keep the tool online 24/7 without your PC being on, you can deploy it to these platforms:

### 1. Koyeb (Recommended)
* Connect your GitHub repository.
* Set the **Run Command** to: `gunicorn app:app`
* Choose the **Nano** instance (Free tier).

### 2. Render
* Connect your GitHub repository.
* Set the **Start Command** to: `gunicorn app:app`
* Render will automatically provide an `https` URL.

### 💡 Note on Procfile
For platforms like Heroku or Koyeb, it is best practice to include a file named `Procfile` (no file extension) in your root directory with the following content:
```text
web: gunicorn app:app


