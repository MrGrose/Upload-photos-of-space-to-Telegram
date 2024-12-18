from pathlib import Path

import requests


def get_epic_image(base_dir: Path, token: str) -> None:
    param = {"api_key": token}
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=param)
    response.raise_for_status()
    text = response.json()

    for number, dates in enumerate(text, 1):
        year, month, day = dates['date'].split()[0].split('-')
        collected_links = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{dates['image']}.png'
        response = requests.get(collected_links, params=param)
        response.raise_for_status()

        with open(base_dir / f'epic_{number}.png', 'wb') as file:
            file.write(response.content)
