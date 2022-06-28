import requests


class Telegram:
    """
    The Telegram for working with telegram notifications
    """
    def __init__(self):

        # Telegram api url to send request
        self.telegram_url = 'https://api.telegram.org/bot'

        # Bot token
        self.token = '5531831428:AAHqoVnCt_6jDSYRgx4HKTl7p1MRrXEeEfE'

        # Make request updates
        response = requests.get('{}{}/getUpdates'.format(self.telegram_url, self.token))

        # Get chat id from updates
        self.chat_id = str(response.json()['result'][0]['message']['from']['id'])

    def telegram_bot_send_message(self, text):

        # Create request to send message to chat
        send_text = '{}{}/sendMessage?chat_id={}&parse_mode=Markdown&text={}'.format(self.telegram_url,
                                                                                     self.token,
                                                                                     self.chat_id,
                                                                                     text)

        # Make request and get response from telegram
        response = requests.get(send_text)

        return response.json()
