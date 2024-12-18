from dotenv import load_dotenv
import os
import telegram


def get_send_messeg(bot, chat_id):
    bot.send_document(chat_id=chat_id, document=open('images/spacex_2.jpg', 'rb'))


def main():
    load_dotenv()
    token = os.getenv('TG_TOKEN')
    bot = telegram.Bot(token)
    chanell = '@test_chanell_768'
    get_send_messeg(bot, chanell)


if __name__ == '__main__':
    main()
