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

    def change(self, phone_old, phone_new):

        phone_old = Phone(phone_old).value
        phone_new = Phone(phone_new).value
        match = False

        for phone in self.phones:

            if phone.value == phone_new:
                return f"{phone_new} already recorded for {self.name.value}"

            if phone.value == phone_old:
                match = True

        if not match:
            return f"{phone_old} exist in the contact {self.name.value}"

        for index, phone in enumerate(self.phones):
            if phone.value == phone_old:
                self.phones.remove(phone)
                self.phones.insert(index, Phone(phone_new))
                return f"{phone_old} changed to {phone_new}"
