
#below,  cart is a container that will store qty, item_name and price. it is not part of inputs.
#so thats why we are using cart afterwards
def add_item(cart = None, item_name = 'Unknown',qty = 1, price = 0.0):

    if cart is None:#if there is no cart create a new car
        cart= []#cart created when there is no one

    for entry in cart:#here we update the cart if there are matching entries(names)
        if entry['name'].lower() == item_name.lower():
            entry["qty"] += qty#if the item name entered matches the item name already in cart we just update by adding quantities
            return cart
    
    new_item = {'name' : item_name, 'qty' : qty, 'price' : price}
    cart.append(new_item)
    return cart


def total_cost(cart):
    total = 0.0
    for entry in cart:#Here we wanna make sure that cost matches the quantity,
        total += entry['qty'] * entry['price']# we multiply quantity and price in our cart
    return round(total, 1)

def print_receipt(cart, curency = 'Ksh'):#extra piece of information — a display option. not adding to a cart. Usefull and easy to change

    print('=========================RECEIPT===================')
    for entry in cart:
        line_total = entry['qty'] * entry['price']  
        print(f'{entry['qty']} × {entry['name']} @ {curency}{entry['price']} = {curency}{line_total}') 
    print('----------------------------------')
    print(f'TOTAL: {curency}{total_cost(cart)}') 

cart = []
add_item(cart, "Apple", 3, 0.5)
add_item(cart, "Bread", 2, 1.5)
add_item(cart, "apple", 2, 0.5)   # duplicate item, quantity increases
add_item(cart, "Milk", 1, 0.99)

print_receipt(cart)
cart2 = add_item()
print_receipt(cart2, curency = 'Ksh')