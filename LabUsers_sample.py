class User:  # کاربر
    first_name: str
    last_name: str
    national_code: str
    username: ...
    password: ...

    gender: str

    def __init__(self, username, passwd, fname, lname, *args):
        self.first_name = fname
        self.last_name = lname
        self.username = username
        self.password = passwd

    def login(self, username, password):
        print("User login method")
        return True or False

    def logout(self):
        ...


class Staff(User):  # کارکنان
    phone: str
    email: str
    zip_code: str

    def __init__(self, username, passwd, fname, lname, phone, email, zip_code, *args):
        super().__init__(username, passwd, fname, lname, *args)
        self.phone = phone
        self.email = email
        self.zip_code = zip_code

    def login(self, phone, password):
        return super().login(phone, password)


class Patient(User):  # بیمار
    blood_type: str


class Doctor(Staff):  # دکتر
    degree: str


class Operator(Staff):  # اپراتور (منشی)
    pass


class Boss(Staff):  # رییس
    pass


akbar = Boss("AkbaBabaii", "akbar99", "akbar", "babaii", "09123456789",
             "asdasdasd@asdas", "123131231")  # اکبر !
akbar.login(akbar.phone, 'akbar99')
