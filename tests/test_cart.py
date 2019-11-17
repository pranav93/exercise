import os
from importlib import reload

import config
from shoppingcart.cart import ShoppingCart


def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 1)

    receipt = cart.print_receipt()

    assert receipt[0] == "apple - 1 - €1.00"


def test_add_item_with_multiple_quantity():
    cart = ShoppingCart()
    cart.add_item("apple", 2)

    receipt = cart.print_receipt()

    assert receipt[0] == "apple - 2 - €2.00"


def test_add_different_items():
    cart = ShoppingCart()
    cart.add_item("banana", 1)
    cart.add_item("kiwi", 1)

    receipt = cart.print_receipt()

    assert receipt[0] == "banana - 1 - €1.10"
    assert receipt[1] == "kiwi - 1 - €3.00"


def test_add_same_item_multiple_times():
    cart = ShoppingCart()
    cart.add_item("banana", 1)
    cart.add_item("kiwi", 1)
    cart.add_item("banana", 1)
    cart.add_item("kiwi", 1)
    cart.add_item("banana", 1)
    cart.add_item("kiwi", 1)

    receipt = cart.print_receipt()

    assert receipt[0] == "banana - 3 - €3.30"
    assert receipt[1] == "kiwi - 3 - €9.00"


def test_set_cart_currency_to_gbp():
    cart = ShoppingCart()
    cart.add_item("apple", 1)

    receipt = cart.print_receipt()

    assert receipt[0] == "apple - 1 - €1.00"

    cart.modify_currency('GBP')
    receipt = cart.print_receipt()

    assert receipt[0] == "apple - 1 - £0.86"


def test_set_product_source_to_dict():
    os.environ["data_source"] = "DICT"
    reload(config)

    cart = ShoppingCart()
    cart.add_item("apple", 1)

    receipt = cart.print_receipt()

    assert receipt[0] == "apple - 1 - €1.00"

    cart.modify_currency('GBP')
    receipt = cart.print_receipt()

    assert receipt[0] == "apple - 1 - £0.86"


def test_check_total():
    cart = ShoppingCart()
    cart.add_item("banana", 1)
    cart.add_item("kiwi", 1)

    receipt = cart.print_receipt()

    assert receipt[-1] == "Total - €4.10"


def test_set_product_source_to_database():
    os.environ["data_source"] = "DATABASE"
    reload(config)

    cart = ShoppingCart()
    cart.add_item("apple", 1)

    receipt = cart.print_receipt()

    assert receipt[0] == "apple - 1 - €1.00"
