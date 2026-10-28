from app import calculate_bill

def test_my_code():
    assert calculate_bill(5.0, 10) == 50.0
    print("TEST PASSED!")

if __name__ == '__main__':
    test_my_code()
from app import calculate_bill

def run_test():
    
    assert calculate_bill(5.0, 10) == 50.0
    print("Push 1 Test Passed Successfully!")

if __name__ == '__main__':
    run_test()
