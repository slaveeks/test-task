import xml.etree.cElementTree as Et
import requests


class Course:
    """
    The Course to convert course
    :param valute_id: id of currency to get course
    :param request_url: url for request to get data
    """
    def __init__(self, valute_id, request_url):

        # Currency id of cb RF
        self.valute_id = valute_id

        # Url for request to get course
        self.request_url = request_url

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
