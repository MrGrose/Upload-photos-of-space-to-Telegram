import argparse


def create_parser() -> 'argparse.ArgumentParser':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='''
        Script for uploading and sending photos from various space APIs
        ''')
    parser.add_argument(
        '-id',
        help='Uploading by id',
    )
    parser.add_argument(
        '-q',
        default=10,
        help='Number of pages to download',
    )
    parser.add_argument(
        '-n',
        help='Sending a photo by number',
    )
    return parser
