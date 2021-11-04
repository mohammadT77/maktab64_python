import pickle


class User:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone

    def save(self):
        file_name = f'{self.id}.user'
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)
        return file_name

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)
