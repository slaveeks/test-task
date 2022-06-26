import xml.etree.cElementTree as ET
import requests


class Course:
    @staticmethod
    def get_usd_course():
        res = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

        tree = ET.fromstring(res.content)

        a = tree.findall('Valute')

        for i in a:
            if i.get('ID') == 'R01235':
                return float(i.find('Value').text.replace(',', '.'))
