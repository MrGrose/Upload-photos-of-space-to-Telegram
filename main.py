import os
from pathlib import Path

from dotenv import load_dotenv
from fetch_spacex_images import fetch_spacex_last_launch
from load_nasa_image import get_nasa_image
from load_epic_image import get_epic_image


def main():
    load_dotenv()
    token = os.getenv('NASA_API_KEY')
    base_dir = Path(__file__).parent / 'images'
    base_dir.mkdir(exist_ok=True)
    fetch_spacex_last_launch(base_dir)
    get_nasa_image(base_dir, token)
    get_epic_image(base_dir, token)


if __name__ == '__main__':
    main()
