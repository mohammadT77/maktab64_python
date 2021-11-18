class MyContextManagerClass:
    def __enter__(self):
        print("Hi, Entering!!!")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Bye, Exiting:")
        print(exc_type, exc_val, exc_tb, sep="|||")
        return True


m = MyContextManagerClass()

with m as enter_return:
    print("enter_return:",enter_return)
    # raise TypeError("dadas", 1, 2, 3, 4)
