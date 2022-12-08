from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    def show_all(self):
        return self.data
    def get_data(self, name):
        return self.data.get(name)


class Field():
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass

class Birthday(Field):
    pass

class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.phone = []
        # self.birthday = Birthday(birthday)
    def put_phone_list(self):
        return self.phone.append(Phone(phone))
