class Customer:
    def __init__(self, first_name, last_name, phone, email) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class BankAccount:
    WAGE_AMOUNT = 600  # کارمزد
    MIN_BALANCE = 10000  # حداقل موجودی

    class MinBalanceError(Exception):
        pass

    def __init__(self, owner: Customer, initial_balance: int = 0) -> None:
        self.__owner = owner  # صاحب حساب
        self.__balance = initial_balance  # موجودی حساب

    def __check_minimum_balance(self, amount_to_withdraw):  # چک کردن حداقل موجودی
        return (self.__balance - amount_to_withdraw) >= self.MIN_BALANCE

    def set_owner(self, owner):  # تغییر صاحب حساب
        self.__owner = owner

    def get_owner(self):  # مشاهده صاحب حساب
        return self.__owner

    def withdraw(self, amount):  # برداشت وجه
        if self.__check_minimum_balance(amount):
            raise BankAccount.MinBalanceError("NOT Enough balance to withdraw!")
        self.__balance -= amount
        self.__balance -= self.WAGE_AMOUNT   # برداشت کارمزد

    def deposit(self, amount):  # واریز وجه
        self.__balance += amount

    def get_balance(self):  # مشاهده موجودی
        self.__balance -= self.WAGE_AMOUNT   # برداشت کارمزد
        return self.__balance

    def transfer(self, target_account, amount: int):  # انتقال وجه
        self.withdraw(amount)  # برداشت از حساب خود
        target_account.deposit(amount)  # واریز به حساب مقصد

    @classmethod
    def change_wage(cls, new_amount):
        cls.WAGE_AMOUNT = max(new_amount, 0)   # حداقل مقدار برابر صفر است

    @classmethod
    def change_min_balance(cls, new_amount):
        cls.MIN_BALANCE = max(new_amount, 0)  # حداقل مقدار برابر صفر است


# Example:
akbar = Customer('Akbar', 'Babaii', '09123456789', 'akbar@gmail.com')
asqar = Customer('Asqar', 'Rezaii', '09123456788', 'asqar@gmail.com')

akbar_account = BankAccount(akbar, 0)
asqar_account = BankAccount(asqar, 1000000)

akbar_account.deposit(25000)
print("Akbar Account balance:", akbar_account.get_balance())

akbar_account.withdraw(10000)
print("Akbar Account balance:", akbar_account.get_balance())

akbar_account.transfer(asqar_account, 10000000)  # ?!