from app import calculate_bill

def run_test():
    
    assert calculate_bill(50.0, 2, 10) == 90.0
    print(" Push 2 Discount Test Passed Successfully!")

if __name__ == '__main__':
    run_test()
