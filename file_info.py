from pathlib import Path
from random import choice


def get_file_info() -> dict[str]:
    base_dir = Path(__file__).parent / 'images'
    photos_name = [photo.name for photo in base_dir.iterdir()]

    photo_name = choice(photos_name)
    file_path = f'images/{photo_name}'

    return {
        'file_name': photo_name,
        'file_path': file_path
        }
