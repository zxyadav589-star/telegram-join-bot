import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Aapka Bot Token
BOT_TOKEN = "8750475954:AAHVZtb-Lt0f9mE2VUK3MJlVr1JR_Kfoh2M"

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    request = update.chat_join_request
    user_id = request.from_user.id
    first_name = request.from_user.first_name
    chat_name = request.chat.title

    try:
        # Join request auto-approve karne ke liye
        await request.approve()

        # User ko DM mein message bhejne ke liye
        message_text = (
            f"<b>{chat_name}</b> is an admin of TITAN 👑, a group you requested to join.\n\n"
            f"Welcome {first_name}!\n\n"
            f"🚨 <b>RAXI GAME HACK How To Activate Hack</b>\n"
            f"Pls Video Ko Pura Dekhna 💯 Setup Video 💯\n\n"
            f"GO! REGISTER ➡️ <a href='https://example.com'>Official Link</a>"
        )

        await context.bot.send_message(
            chat_id=user_id,
            text=message_text,
            parse_mode='HTML',
            disable_web_page_preview=False
        )

    except Exception as e:
        print(f"Error sending message to user {user_id}: {e}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(handle_join_request))
    print("Bot chalu ho gaya hai...")
    app.run_polling()

if __name__ == '__main__':
    main()
