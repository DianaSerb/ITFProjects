def my_unit_test(func):
    def wrapper(a):
        print(f"My unit test started for {a}")
        func(a)
        print("Unit test is finished.")

    return wrapper
