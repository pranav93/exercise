from shoppingcart.cart import ShoppingCart

cart = ShoppingCart()
cart.add_item("apple", 1)
cart.add_item("banana", 1)
cart.add_item("kiwi", 1)
cart.add_item("potato", 1)

receipt = cart.print_receipt()
print(receipt)

cart.modify_currency('GBP')
receipt = cart.print_receipt()
print(receipt)

cart.modify_currency('USD')
receipt = cart.print_receipt()
print(receipt)

cart.modify_currency('INR')
receipt = cart.print_receipt()
print(receipt)
