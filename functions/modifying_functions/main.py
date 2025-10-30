def apply_discount(price, discount=0.05):
    discounted_price = price * (1-discount)
    return discounted_price

def apply_tax(discounted_price, tax=0.07):
    taxed_price = discounted_price * (1+tax)
    return taxed_price

def calculate_total(price, discount=0.05, tax=0.07):
    discounted_price = apply_discount(price, discount)
    total_price = apply_tax(discounted_price, tax)
    return total_price

calculate_total(120)

print(f"Total cost with default discount and tax: ${calculate_total(120)}")
calculate_total(100, discount=0.1, tax=0.08)
print(f"Total cost with custom discount and tax: ${calculate_total(100, discount=0.1, tax=0.08)}")
    