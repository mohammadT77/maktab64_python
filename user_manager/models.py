import pickle
from exceptions import UserError, LoginError


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