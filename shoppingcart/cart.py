import typing
from collections import OrderedDict

from shoppingcart.currencies import Currencies
from shoppingcart.products import Products
from . import abc


class ShoppingCart(abc.ShoppingCart):
    def __init__(self):
        default_currency_code = 'EUR'
        self._items = OrderedDict()
        self._products = Products()
        self._currencies = Currencies(default_currency_code)

    def add_item(self, product_code: str, quantity: int):
        if product_code not in self._items:
            self._items[product_code] = quantity
        else:
            q = self._items[product_code]
            self._items[product_code] = q + quantity

    def print_receipt(self) -> typing.List[str]:
        lines = []
        total_price = 0
        currency_sign = self._currencies.currency_sign

        for item in self._items.items():
            price = self._products.get_product_price(item[0]) * item[1]
            price = self._currencies.convert_to(price)

            price_string = "%s%.2f" % (currency_sign, price)
            total_price += price

            lines.append(item[0] + " - " + str(item[1]) + ' - ' + price_string)

        lines.append("Total - %s%.2f" % (currency_sign, total_price))

        return lines

    def modify_currency(self, currency_code: str):
        self._currencies.set_currency(currency_code)
