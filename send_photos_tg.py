import telegram


def send_photo(
    bot: 'telegram.bot.Bot',
    channel: str,
    file_info: dict[str],
     ) -> None:

    bot.send_photo(channel, photo=open(file_info['file_path'], 'rb'),
                   caption=file_info['file_name'])
