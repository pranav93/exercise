
import abc
import typing


class ShoppingCart(abc.ABC):

    @abc.abstractmethod
    def add_item(self, product_code: str, quantity: int):
        pass

    @abc.abstractmethod
    def print_receipt(self) -> typing.List[str]:
        pass


class Products(abc.ABC):

    @abc.abstractmethod
    def get_product_price(self, product_code: str) -> float:
        pass


class Currencies(abc.ABC):

    @abc.abstractmethod
    def convert_to(self, value: float) -> float:
        pass

    @abc.abstractmethod
    def set_currency(self, currency_code: str):
        pass
