from dotenv import load_dotenv
import os
import telegram
from time import sleep
from delay import time_convector
from file_info import get_file_info


def send_photo(
    bot: 'telegram.bot.Bot',
    channel: str,
    file_info: dict[str],
     ) -> None:

    bot.send_photo(channel, photo=open(file_info['file_path'], 'rb'),
                   caption=file_info['file_name'])


def main():
    load_dotenv()
    token_tg = os.getenv('TG_TOKEN')
    bot = telegram.Bot(token_tg)
    channel = '@test_chanell_768'
    delay = 0.002
    while True:
        file_info = get_file_info()
        send_photo(bot, channel, file_info)
        sleep(time_convector(delay))


if __name__ == '__main__':
    main()
