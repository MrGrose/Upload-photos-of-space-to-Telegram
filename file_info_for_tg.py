from pathlib import Path
from random import choice


def get_file_info(number_photo: str) -> dict[str]:

    base_dir = Path(__file__).parent / 'images'
    photos_name = [photo.name for photo in base_dir.iterdir()]

    if not number_photo:
        photo_name = choice(photos_name)
        file_path = f'images/{photo_name}'
        return {
            'file_name': photo_name,
            'file_path': file_path
            }

    else:
        return {
            'file_name': photos_name[int(number_photo)],
            'file_path': f'images/{photos_name[int(number_photo)]}'
            }
