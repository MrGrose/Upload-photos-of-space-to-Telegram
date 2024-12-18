from dotenv import load_dotenv
import os
import telegram


def get_send_messeg(bot, chat_id):
    text = "Первое сообщение"
    send_chanel = bot.send_message(chat_id=chat_id, text=text)
    print(f'Номер отправленного сообщения: {send_chanel.message_id}')


def main():
    load_dotenv()
    token = os.getenv('TG_TOKEN')
    bot = telegram.Bot(token)
    chanell = '@test_chanell_768'
    get_send_messeg(bot, chanell)


if __name__ == '__main__':
    main()
