import argparse


def create_parser() -> 'argparse.ArgumentParser':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'id',
        nargs='?',
        help='Загрузка по id, если он передан',
        type=str
    )
    parser.add_argument(
        'quantity',
        nargs='?',
        default=10,
        help='Количество страниц для загрузки',
        type=int
    )
    return parser
