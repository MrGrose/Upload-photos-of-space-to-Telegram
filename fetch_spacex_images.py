import random
from pathlib import Path

import requests


def fetch_spacex_last_launch(base_dir: Path, id: str = None) -> None:
    urls = []
    if id:
        url = f'https://api.spacexdata.com/v5/launches/{id}'
    else:
        url = 'https://api.spacexdata.com/v5/launches'

    response = requests.get(url)
    response.raise_for_status()

    if id:
        urls = response.json()['links']['flickr']['original']
    else:
        for link_for_lst in response.json():
            flickr_links = link_for_lst['links']['flickr']['original']
            if flickr_links:
                urls.append(flickr_links)

        urls = random.choice(urls)

    for link_number, link in enumerate(urls, 1):
        with open(base_dir / f'spacex_{link_number}.jpg', 'wb') as file:
            response_link = requests.get(link)
            response_link.raise_for_status()
            file.write(response_link.content)
