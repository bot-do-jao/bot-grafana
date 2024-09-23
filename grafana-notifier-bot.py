import logging

from telegram import (
    Update,
    ForceReply,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ParseMode,
)
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    CallbackQueryHandler,
)

logger = logging.getLogger(__name__)


def forward_to_group(update: Update, context: CallbackContext) -> None:
    """
    This function forwards all received messages to the target group chat and logs them.
    """
    group_chat_id = CHAT_ID  # Replace with your actual group chat ID
    message_text = update.message.text  # Extract message text

    # Log the message
    logging.info(f"Received message: {message_text}")

    update.message.forward(chat_id=group_chat_id)


def main() -> None:
    updater = Updater("BOT_ID")

    # Get the dispatcher to register handlers
    # Then, we register each handler and the conditions the update must meet to trigger it
    dispatcher = updater.dispatcher

    # Configure logging
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    # Forward all messages (except commands) to the group and log them
    dispatcher.add_handler(MessageHandler(~Filters.command, forward_to_group))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == "__main__":
    main()
