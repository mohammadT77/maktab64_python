import pickle


class User:
    def __init__(self, id, username, name, phone, password, email=None):
        self.__check_data(id, username, name, phone, password, email)
        self.id = id
        self.username = username
        self.name = name
        self.phone = phone
        self.password = password
        self.email = email

    def __check_data(self, id, username: str, name, phone, password, email=None):
        if not isinstance(id, int) or id < 0:
            raise UserError("Id invalid", 'id', id)
        if not username.lower() or len(username) < 8:
            raise UserError("Username must be longer than 8 chars", 'username', username)
        ...
        if len(password) < 8:
            raise UserError("Password must be longer than 8 chars", 'password', "...")

    def save(self):
        file_name = f'{self.username}.user'
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)
        return file_name

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)

    @classmethod
    def login(cls, username: str, password: str):
        """
        Login an user by Username & Password
        :param username: str
        :param password: str
        :return User
        """

        # Fetching User from files!
        file_path = f"{username}.user"
        try:
            user = cls.from_file(file_path)
        except FileNotFoundError:
            raise LoginError("username", "User is not exist!")

        # Validate password!
        if user.password != password:
            raise LoginError("password", "Password not matched!")

        return user


class UserError(Exception):

    def __init__(self, msg: str, field: str, data: ...) -> None:
        super().__init__(msg, field, data)
        self.msg = msg
        self.field = field
        self.data = data

    def __str__(self):
        return f"error on field `{self.field}` (invalid data: `{self.data}`): {self.msg}"

class LoginError(Exception):

    def __init__(self, reason, msg, *args) -> None:
        super().__init__(reason, msg, *args)


def register_menu():
    print("RegisterMenu")
    print("Enter your profile below:")

    id = input(">> id:")
    username = input(">> username:")
    name = input(">> name:")
    phone = input('>> phone:')
    password = input('>> password:')
    email = input('>> email(opt):')

    try:
        user = User(int(id), username, name, phone, password, email)
        file = user.save()
        print(f"User Registered (file: {file})")
    except UserError as e:
        print("Error:", e, "\nTry again!!!\n")
        register_menu()

def login_menu():
    print("LoginMenu")
    print("Enter your username & password:")

    username = input(">> username:")
    password = input('>> password:')

    try:
        user = User.login(username, password)
        print("Welcome: ", user)
    except LoginError as e:
        print("Error:", e)
        login_menu()

def main_menu():
    print("UserManager")
    print(">> 1. Login")
    print(">> 2. Register")

    opt = input("Enter your option: ")
    if opt == '1':
        login_menu()
    elif opt == '2':
        register_menu()
    else:
        print("Invalid option\n")
        main_menu()

main_menu()