from pathlib import Path

import requests
from get_file_info import get_expansion_file


def get_nasa_image(base_dir: Path, token: str, quantity: int = 10) -> None:
    param = {'count': quantity,
             "api_key": token}
    url = 'https://api.nasa.gov/planetary/apod'

    response = requests.get(url, params=param)
    response.raise_for_status()
    text_nasa = response.json()

    for number, link in enumerate(text_nasa, 1):
        image_url = link['url']
        name_expansion, is_image = get_expansion_file(image_url)

        if is_image:
            new_path = base_dir / f'nasa_apod_{number}{name_expansion}'
            links = requests.get(link['url'])
            response.raise_for_status()

            with open(new_path, 'wb') as file:
                file.write(links.content)
        else:
            print(f"Пропускаем не изображение: {image_url}")
