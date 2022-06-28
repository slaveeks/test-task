import requests


class Telegram:

    def __init__(self):
        response = requests.get('https://api.telegram.org/bot5531831428:AAHqoVnCt_6jDSYRgx4HKTl7p1MRrXEeEfE/getUpdates')
        self.chat_id = str(response.json()['result'][0]['message']['from']['id'])

    def telegram_bot_sendtext(self):
        send_text = 'https://api.telegram.org/bot' + '5531831428:AAHqoVnCt_6jDSYRgx4HKTl7p1MRrXEeEfE' + '/sendMessage?chat_id=' + self.chat_id + '&parse_mode=Markdown&text=' + 'no!'

        response = requests.get(send_text)

        return response.json()
