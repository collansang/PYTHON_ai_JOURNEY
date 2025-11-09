def get_total(qty, price):
    return qty * price

def apply_dic(total, discount= 5):
    return total - (total * (discount/100))

total = get_total(2, 120)
disc_total = apply_dic(total , 7)
print(disc_total)