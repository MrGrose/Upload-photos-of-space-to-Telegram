import os
from pathlib import Path

from arg_parser import create_parser
from dotenv import load_dotenv
from fetch_spacex_images import fetch_spacex_last_launch
from load_epic_image import get_epic_image
from load_nasa_image import get_nasa_image


def main():
    load_dotenv()
    token = os.getenv('NASA_API_KEY')
    base_dir = Path(__file__).parent / 'images'
    base_dir.mkdir(exist_ok=True)
    parser = create_parser()
    parsed_args = parser.parse_args()
    if parsed_args.id is not None and parsed_args.id.isdigit():
        parsed_args.quantity = int(parsed_args.id)
        parsed_args.id = None

    fetch_spacex_last_launch(base_dir, parsed_args.id)
    get_nasa_image(base_dir, token, parsed_args.quantity)
    get_epic_image(base_dir, token)


if __name__ == '__main__':
    main()
