from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# In-memory storage (for simplicity)
users_data = {}

# Start command to send the Web App button
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    web_app_url = "http://127.0.0.1:5500/frontapp.html"  # Replace with your hosted web app URL

    # Create a button that opens the Web App
    keyboard = [
        [InlineKeyboardButton("Open Mini App", web_app={"url": web_app_url})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome! Click the button to start the Bet:",
        reply_markup=reply_markup
    )

# Handle data submitted from the Web App
async def handle_web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query and query.web_app_data:
        # Extract the submitted data
        data = query.web_app_data.data
        user_id = query.from_user.id

        # Save the data in memory
        users_data[user_id] = data

        # Acknowledge the data submission
        await query.answer()
        await query.message.reply_text(f"Registration successful! Your data: {data}")

# Main function to set up the bot
def main():
    application = ApplicationBuilder().token("7557465715:AAFilKSpYGTD6vZ-EkJqcQVqPfKi7stlfxw").build()

    # Add handlers for the bot
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_web_app_data))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
