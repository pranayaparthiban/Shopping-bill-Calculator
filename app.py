def calculate_bill(price, quantity):
    return price * quantity

if __name__ == '__main__':
    price = 50.0
    quantity = 3
    
    total = calculate_bill(price, quantity)
    print(f"Price: {price} | Quantity: {quantity}")
    print(f"Total Bill: {total}")
