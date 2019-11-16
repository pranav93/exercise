from . import abc

from data import currency_info


class Currencies(abc.Currencies):
    def __init__(self, currency_code):
        '''
        Init method for currency
        :param currency_code: target currency code e.g. GBP, INR
        '''
        self.currency_code = ''
        self.currency_sign = ''
        self.set_currency(currency_code)
        self._exchange_rate = currency_info.exchange_rate

    def convert_to(self, value: float) -> float:
        '''
        This method converts the provided EUR value in given currency code
        :param value: The value in EUR to be converted
        :return: converted value
        '''
        return value * self._exchange_rate[self.currency_code]

    def set_currency(self, currency_code: str):
        '''
        This method modifies the currency code
        :param currency_code: target currency code e.g. GBP, INR
        '''
        self.currency_code = currency_code
        self.currency_sign = currency_info.currency_signs[currency_code]
