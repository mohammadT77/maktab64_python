from abc import ABC


class DBModel(ABC):
    TABLE: str
    PK: str

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} {vars(self)}>"


class Patient(DBModel):
    TABLE = 'patient'
    PK = 'id'

    def __init__(self, first_name, last_name, phone, national_id, age, id=None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.national_id = national_id
        self.age = age
        if id: self.id = id
