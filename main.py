import logging
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Aapka Bot Token
BOT_TOKEN = "8750475954:AAHVZtb-Lt0f9mE2VUK3MJlVr1JR_Kfoh2M"

# -------------------------------------------------------------
# CONFIGURATION (Aapke links aur username):
# -------------------------------------------------------------
VIDEO_URL = "https://t.me/c/2540430712/4242"
APK_URL = "https://t.me/c/2540430712/4243"
SUPPORT_USERNAME = "Krix_Trader"
# -------------------------------------------------------------

# Render ke port error ko fix karne ke liye dummy web server
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"1LVL FIXXER Bot is running!")

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    request = update.chat_join_request
    user_id = request.from_user.id
    first_name = request.from_user.first_name
    chat_name = request.chat.title

    try:
        # 1. Join Request Auto-Approve Karein
        await request.approve()

        # -------------------------------------------------------------
        # 2. MESSAGE 1: VIP Setup Video
        # -------------------------------------------------------------
        video_caption = (
            f"👑 <b>{chat_name}</b> is an admin of <b>1LVL FIXXER</b>, a group you requested to join.\n\n"
            f"👋 Welcome <b>{first_name}</b>!\n\n"
            f"🚨 <b>1LVL FIXXER VIP HACK ACTIVATION GUIDE</b>\n"
            f"Pls Video Ko Pura Dekhna 💯 Setup Video 💯\n\n"
            f"🔥 <b>STATUS:</b> <a href='https://t.me/{SUPPORT_USERNAME}'>WORKING 100% (UNDETECTED)</a>"
        )

        await context.bot.send_video(
            chat_id=user_id,
            video=VIDEO_URL,
            caption=video_caption,
            parse_mode='HTML'
        )

        # -------------------------------------------------------------
        # 3. MESSAGE 2: VIP MOD APK Document File
        # -------------------------------------------------------------
        apk_caption = (
            f"📦 <b>1LVL_FIXXER_MOD_APK.apk</b>\n"
            f"⚡ <i>2.2 MB - Anti-Ban Latest Version</i>\n\n"
            f"🚨 <b>1LVL FIXXER GAME HACK How To Activate Hack</b>\n"
            f"Pls Video Ko Pura Dekhna 💯 Setup Video 💯"
        )

        await context.bot.send_document(
            chat_id=user_id,
            document=APK_URL,
            caption=apk_caption,
            parse_mode='HTML'
        )

        # -------------------------------------------------------------
        # 4. MESSAGE 3: Text Status & Live Support Button
        # -------------------------------------------------------------
        keyboard = [
            [InlineKeyboardButton("💬 LIVE CHAT SUPPORT", url=f"https://t.me/{SUPPORT_USERNAME}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        text_message = "WORKING NOT 101% 🔥"

        await context.bot.send_message(
            chat_id=user_id,
            text=text_message,
            parse_mode='HTML',
            reply_markup=reply_markup
        )

    except Exception as e:
        print(f"Error sending message to user {user_id}: {e}")

def main():
    # Web server ko background mein start karein taaki Render port detect kar sake
    server_thread = Thread(target=run_web_server)
    server_thread.daemon = True
    server_thread.start()

    # Telegram bot start karein
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(handle_join_request))
    print("1LVL FIXXER Bot start ho gaya hai...")
    app.run_polling()

if __name__ == '__main__':
    main()
