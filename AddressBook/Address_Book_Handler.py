from AddressBook.addressbook import *
from abc import abstractmethod, ABC


class AddressBot:
    def __init__(self):
        self.book = AddressBook()


class Command(ABC):
    @abstractmethod
    def processing(self):
        pass


class Add(Command):
    def processing(self, data_container: AddressBot):
        name = Name().value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        address = Address().value
        record = Record(name, phones, birth, email, address)
        data_container.book.save("logs\\address_book_auto_save")
        return data_container.book.add(record)


class Search(Command):
    def processing(self, data_container: AddressBot):
        category = input("Enter a search category (Name/Phone/Email/Address/Birthday) : ").strip().lower().replace(" ", "")
        search_parameter = input("Enter the search parameter: ").strip().lower().replace(" ", "")
        result = data_container.book.search(category, search_parameter)
        return result


class Edit(Command):
    def processing(self, data_container: AddressBot):
        contact_data = input("Enter any data about contact that you want to change: ")
        new_category = input("Enter a category (Name/Phone/Address/Email/Birthday): ").strip().lower().capitalize()
        data_container.book.save("logs\\address_book_auto_save")
        return data_container.book.edit(contact_data, new_category)


class Delete(Command):
    def processing(self, data_container: AddressBot):
        contact_info_to_remove = input("Enter any data about contact that you want to delete: ").strip().lower()
        data_container.book.save("logs\\address_book_auto_save")
        return data_container.book.delete(contact_info_to_remove)


class Save(Command):
    def processing(self, data_container: AddressBot):
        file_name = input("Enter the filename: ")
        return data_container.book.save(file_name)


class Load(Command):
    def processing(self, data_container: AddressBot):
        path = input('Enter the filename: ')
        return data_container.book.load(path)


class Congratulate(Command):
    def processing(self, data_container: AddressBot):
        try:
            days_range = int(input('Enter the range of days: '))
            return data_container.book.congratulate(days_range)
        except ValueError:
            print('Incorrect format of days range! It must be an integer!')



class Show(Command):
    def processing(self, data_container: AddressBot):
        return data_container.book.show()


class Help(Command):
    def processing(self, data_container: AddressBot):
        return data_container.book.help_me()


        


COMMANDS = {
    "help": Help,
    "add": Add,
    "search": Search,
    "edit": Edit,
    "delete": Delete,
    "save": Save,
    "load": Load,
    "congratulate": Congratulate,
    "show": Show,
}


def get_handler(action):
    for command in COMMANDS.keys():
        if action in command:
            return COMMANDS[command]()


def performer(command: Command, data_container: AddressBot):
    return command.processing(data_container)













