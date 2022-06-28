import xml.etree.cElementTree as Et
import requests


class Course:
    """
    The Course to convert course
    """

    def __init__(self):

        # Currency id of cb RF
        self.valute_id = 'R01235'

        # Url for request to get course
        self.request_url = 'http://www.cbr.ru/scripts/XML_daily.asp'

    def get_usd_course(self):
        """
        Get USD course
        :return: float
        """

        # Send request to get data
        res = requests.get(self.request_url)

        # Parse xml
        tree = Et.fromstring(res.content)

        # Get currencies
        currencies = tree.findall('Valute')

        for currency in currencies:

            # Find currency by id
            if currency.get('ID') == self.valute_id:
                # Get value, convert to float
                return float(currency.find('Value').text.replace(',', '.'))

    def convert_from_usd_to_rub(self, usd):
        """
        Convert from USD to RUB
        :param usd: data to convert
        :return: float
        """
        return "{:.2f}".format(self.get_usd_course() * usd)
