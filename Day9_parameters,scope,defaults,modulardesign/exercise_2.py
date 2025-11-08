def add_item(cart = None, item_name = 'Unknown',qty = 1, price = 0.0, discount = 0.05):

    if cart is None:
        cart= []

    for entry in cart:
        if entry['name'].lower == item_name.lower():
            entry["qty"] += qty
        return cart
    
    new_item = {'name' : item_name, 'qty' : qty, 'price' : price, 'dsc' : discount}
    cart.append(new_item)
    return cart

cart = []

add_item(cart, 'apple', 3, 76, 0)
add_item(cart, 'orrange', 2, 34)
add_item(cart, 'pineapple', 7, 34)
add_item(cart, 'apple', 1, 34, 0)
add_item(cart, 'banana', 3, 34, 0)

for c in cart:
    print(c)