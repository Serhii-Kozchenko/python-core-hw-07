from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            self.value = value
        else:
            raise ValueError("Number must have 10 numbers and contain only digits")

    def __str__(self):
        return str(self.value)


class Record(Field):
    def __init__(self, name):

        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday:str):
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return i
        return None
    


    def remove_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)

    def edit_phone(self, phone, new_phone):
        for i in range(len(self.phones)):
            if self.phones[i].value == phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError
         
          

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}, birthday: {str(self.birthday)}"
 
    
class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except:
            raise ValueError
    
        


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    
    
  
        



    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values()) 



