from addressbook import *
from abc import abstractmethod, ABC


class AddressBot:
    def __init__(self):
        self.book = AddressBook()


class Command(ABC):
    @abstractmethod
    def processing(self):
        pass


class Add(Command):
    def processing(self, data_container: AddressBook):
        name = Name().value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        address = Address().value
        record = Record(name, phones, birth, email, address)
        data_container.book.save("logs\\address_book_auto_save")
        return data_container.book.add(record)


class Search(Command):
    def processing(self, data_container: AddressBook):
        category = input("Enter a search category (Name/Phone/Email/Address/Birthday) : ").strip().lower().replace(" ", "")
        search_parameter = input("Enter the search parameter: ").strip().lower().replace(" ", "")
        result = data_container.book.search(category, search_parameter)
        return result


class Edit(Command):
    def processing(self, data_container: AddressBook):
        contact_data = input("Enter any data about contact that you want to change: ")
        new_category = input("Enter a category (Name/Phone/Address/Email/Birthday): ").strip().lower().capitalize()
        data_container.book.save("logs\\address_book_auto_save")
        return data_container.book.edit(contact_data, new_category)


class Delete(Command):
    def processing(self, data_container: AddressBook):
        contact_info_to_remove = input("Enter any data about contact that you want to delete: ").strip().lower()
        data_container.book.save("logs\\address_book_auto_save")
        return data_container.book.delete(contact_info_to_remove)


class Save(Command):
    def processing(self, data_container: AddressBook):
        file_name = input("Enter the filename: ")
        return data_container.book.save(file_name)


class Load(Command):
    def processing(self, data_container: AddressBook):
        path = input('Enter the filename: ')
        return data_container.book.load(path)


class Congratulate(Command):
    def processing(self, data_container: AddressBook):
        try:
            days_range = int(input('Enter the range of days: '))
            return data_container.book.congratulate(days_range)
        except ValueError:
            print('Incorrect format of days range! It must be an integer!')



class Show(Command):
    def processing(self, data_container: AddressBook):
        return data_container.book.show()


class Help(Command):
    def processing(self, data_container: AddressBook):
        address_book_docs = {
            'Add' : 'add contact',
            'Search' : 'search contact using any information',
            'Edit' : 'edit recorded contact',
            'Delete' : 'delete existing contact',
            'Save' : 'save your contact book to the file',
            'Load' : 'recover contacts from the file',
            'Congratulate' : 'find out who you need to congratulate in the near future',
            'Show' : 'print all contacts that you have'
        }
        table = PrettyTable()
        table.field_names = ['Command', 'Description']
        for command, description in address_book_docs.items():
            table.add_row([command, description])
        return table


        


COMMANDS = {
    ("add",): Add,
    ("search",): Search,
    ("edit",): Edit,
    ("delete",): Delete,
    ("save",): Save,
    ("load",): Load,
    ("congratulate",): Congratulate,
    ("show",): Show,
    ("help",): Help
}


def get_handler(action):
    for command_container in COMMANDS.keys():
        for command in command_container:
            if action in command:
                return COMMANDS[command_container]()


def performer(command: Command, data_container: AddressBot):
    return command.processing(data_container)












