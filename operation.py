from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):

        if not isinstance(value, str):
            raise ValueError('Value must be a string')
        self.value = value

    def __str__(self) -> str:
        return str(self.value)
    
    def __repr__(self) -> str:
        return str(self)
    
    


class Record(Field):

    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phones = [phone] if phone else []
        self.birthday = birthday
    
    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone(self, old_phone, new_phone):

        for i, p in enumerate(self.phones):
            if p.value == old_phone.value:
                self.phones[i] = new_phone

        return f'Change {old_phone} to {new_phone}'
    
    def add_birthday(self, birthday):
        self.birthday = birthday
    
    def days_to_birthday(self):

        today = datetime.now()
        if self.birthday:
            days_delta = (self.birthday.value.date().replace(year=today.year) - today.date()).days
            return f'His birthday will be after {days_delta} days' if days_delta >= 0 else f'His birthday was {days_delta*-1} days ago'
            
        return f'{self.name} not have birthdate'

    
class Phone(Field):

    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise ValueError('Must be a interger')
        if len(str(value)) != 12:
            raise ValueError('Number must have only 12 number')
        self.__value = value


class Name(Field):

    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            raise ValueError('Must be a string')
        if len(value) < 2 and len(value) > 15:
            raise ValueError('Number must have only 12 number')
        self.__value = value


class Birthday(Field):

    def __init__(self, value):

        try:
            self.value = datetime.strptime(value, '%Y.%m.%d')
        except ValueError:
            print('It is not a data. Try year.month.day')

            
class AdressBook(UserDict):
    def add_contact(self, contact:Record):
        self.data[contact.name.value] = contact

    def paginator(self, iter_obj, page=2):
        start = 0

        while True:
            
            result_keys = list(iter_obj)[start:start + page]
            result = ' '.join([f'{k}: {iter_obj.get(k).phones}' for k in result_keys])
            if not result:
                break
            yield result
            start += page
        



if __name__ == '__main__':
    adress_book = AdressBook()
