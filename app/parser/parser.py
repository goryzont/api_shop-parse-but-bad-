import requests
import re
import csv

from app.parser.model import Items
from app.config import settings

import psycopg2


class ParseWB:

    def __init__(self, url: str):
        self.brand_id = self.__get_brand_id(url)

    @staticmethod
    def __get_brand_id(url: str):
        regex = "(?<=brandpage=).+(?=__)"
        brand_id = re.search(regex, url)[0]
        return brand_id

    def parse(self):
        i = 1
        params = {
            'brand': f'{self.brand_id}',
            'limit': '300',
            'sort': 'popular',
            'page': f'{i}',
            'appType': '128',
            'curr': 'rub',
            'lang': 'ru',
            'dest': '-59208',
            'spp': '27',
            'TestGroup': 'no_test',
            'TestID': 'no_test',
        }

        while True:
            response = requests.get('https://catalog.wb.ru/brands/m/v1/catalog', params=params)
            print(response.status_code)
            #response.encoding = 'utf-8-sig'
            i += 1
            items_info = Items.model_validate(response.json()['data'])
            if not items_info.products:
                break
            self.__add_in_db(items_info)

    def __add_in_db(self, items: Items):
        conn = psycopg2.connect(database=f'{settings.DB_NAME}',
                                user=f'{settings.DB_USER}',
                                password=f'{settings.DB_PASS}',
                                host=f'{settings.DB_HOST}')

        with conn:
            with conn.cursor() as curs:
                for product in items.products:
                    # if ' ' in product.name:
                    #     product.name = product.name.replace(" ", '')
                    # if ' ' in product.supplier:
                    #     product.supplier = product.supplier.replace(" ", '')
                    query = f"INSERT INTO product (id, name, provider, price, quantity)VALUES ({product.id}, '{product.name}', '{product.supplier}', {product.salePriceU}, {product.volume});"
                    curs.execute(query)
                    conn.commit()





