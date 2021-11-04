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

    def __check_data(self,  id, username:str, name, phone, password, email=None):
        if not isinstance(id, int) or id < 0:
            raise UserError("Id invalid", 'id',id)
        if not username.lower() or len(username) < 8:
            raise UserError("Username must be longer than 8 chars", 'username', username)
        ...
        if len(password) < 8:
            raise UserError("Password must be longer than 8 chars", 'password', "...")

    def save(self):
        file_name = f'{self.id}.user'
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)
        return file_name

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)


class UserError(Exception):

    def __init__(self, msg: str, field: str, data: ...) -> None:
        super().__init__(msg, field, data)
        self.msg = msg
        self.field = field
        self.data = data

    def __str__(self):
        return f"error on field `{self.field}` (invalid data: `{self.data}`): {self.msg}"