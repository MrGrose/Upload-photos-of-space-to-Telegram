import os
from pathlib import Path
from time import sleep

import telegram
from arg_parser import create_parser
from delay_for_tg import time_convector
from dotenv import load_dotenv
from fetch_spacex_images import fetch_spacex_last_launch
from file_info_for_tg import get_file_info
from load_epic_images import get_epic_image
from load_nasa_images import get_nasa_image
from send_photos_tg import send_photo


def main():
    load_dotenv()
    token = os.getenv('NASA_API_KEY')
    base_dir = Path(__file__).parent / 'images'
    base_dir.mkdir(exist_ok=True)
    token_tg = os.getenv('TG_TOKEN')
    bot = telegram.Bot(token_tg)
    channel = '@test_chanell_768'
    delay = 4
    parser = create_parser()
    parsed_args = parser.parse_args()

    fetch_spacex_last_launch(base_dir, parsed_args.id)
    get_nasa_image(base_dir, token, parsed_args.q)
    get_epic_image(base_dir, token)

    while True:
        file_info = get_file_info(parsed_args.n)
        send_photo(bot, channel, file_info)
        sleep(time_convector(delay))


if __name__ == '__main__':
    main()
