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
    def __init__(self, value):
        # super().__init__(name)
        self.value = value

class Phone(Field):
    def __init__(self, value):
        # super().__init__(phone)
        self.value = value

class Birthday(Field):
    pass

class Record():
    def __init__(self, name, *phones):
        self.name = Name(name)
        self.phones = []
        if phones:
            for phone in phones:
                self.put_phone_list(phone)
        # self.birthday = Birthday(birthday)
    
    def put_phone_list(self, phone_new):
        phone_new = Phone(phone_new).value
        for phone in self.phones:
            if phone_new == phone.value:
                print(f"{phone_new} already recorded for {self.name.value}")
        self.phones.append(Phone(phone_new))
