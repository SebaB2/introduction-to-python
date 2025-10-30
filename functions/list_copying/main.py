def apply_discount(prices):
    prices_copy = prices.copy()
    for n in range(len(prices_copy)):
        if prices_copy[n] > 2.00:
            new_price = prices_copy[n] * (1-0.1)
            prices_copy[n] = new_price
    return prices_copy





# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)
print(f"Updated product prices: {updated_prices}")