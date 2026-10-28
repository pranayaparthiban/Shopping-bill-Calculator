def calculate_bill(price, quantity, discount_percentage=0):
    subtotal = price * quantity
    discount_amount = subtotal * (discount_percentage / 100)
    return subtotal - discount_amount

if __name__ == '__main__':
    
    price = 50.0
    quantity = 3
    discount = 10  
    
    
    total = calculate_bill(price, quantity, discount)
    print(f"Price: {price} | Quantity: {quantity} | Discount: {discount}%")
    print(f"Total Bill (After Discount): {total}")
