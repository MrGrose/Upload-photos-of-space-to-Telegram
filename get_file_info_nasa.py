import os


def get_expansion_file(url) -> tuple:
    _, ext = os.path.splitext(url)
    ext_lower = ext.lower()
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    is_image = ext_lower in valid_extensions

    return ext_lower, is_image
