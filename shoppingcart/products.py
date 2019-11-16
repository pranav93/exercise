import json

from . import abc
import config
from data import product_info


class Products(abc.Products):
    def __init__(self):
        self._products = dict()
        data_source = config.data_source
        self._load_data(data_source)

    def _load_data(self, data_source: str):
        if data_source == 'JSON':
            self._load_data_from_json()
        if data_source == 'DATABASE':
            raise NotImplementedError('This is yet to be implemented')
        if data_source == 'DICT':
            self._load_data_from_dict()

    def _load_data_from_json(self):
        with open('./data/product_info.json') as f:
            self._products = json.loads(f.read())

    def _load_data_from_dict(self):
        self._products = product_info.products

    def _load_data_from_database(self):
        pass

    def get_product_price(self, product_code: str) -> float:
        return self._products.get(product_code, 0.0)
