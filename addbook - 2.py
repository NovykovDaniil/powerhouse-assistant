import datetime
import os.path
import pickle


class Record:
    def __init__(self, name, address, phone, email, birthday):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.birthday = birthday

    def __str__(self):
        return f'{self.name} - {self.address}, {self.phone}, {self.email}, {self.birthday}'


class AddressBook:
    def __init__(self):
        self.records = []
        self.filename = "address_book.pkl"

        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                self.records = pickle.load(f)

        self._save()

    def add(self, record):
        self.records.append(record)
        self._save()

    def _save(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.records, f)

    def validate_phone_number(self, phone):
        if len(phone) != 12:
            return False
        if not phone[:3].isdigit() or not phone[4:7].isdigit() or not phone[8:].isdigit():
            return False
        if phone[3] != '-' or phone[7] != '-':
            return False
        return True

    def validate_email(self, email):
        if '@' not in email:
            return False
        if '.' not in email.split('@')[1]:
            return False
        return True

    # Редагувати контакт

    def edit_contact(self, index, record):
        if not self.validate_phone_number(record.phone):
            print("The number is not correct.")
        elif not self.validate_email(record.email):
            print("The email is not correct.")
        else:
            self.records[index] = record
            self._save()
            print("Contact edited.")

    # Видалити контакт
    def delete_contact(self, index):
        del self.records[index]
        self._save()
        print("Contact deleted.")

    # Пошук контактів
    def search_contacts(self):
        search_query = input("Enter search string: ")
        results = []
        for record in self.records:
            contact_info = [
                record.name,
                record.phone,
                record.email,
                record.birthday
            ]

            if any(search_query.lower() in str(info).lower() for info in contact_info):
                results.append(record)

        if len(results) == 0:
            print("No contacts found")
        else:
            print(f"Found {len(results)} contacts:")
            for result in results:
                print(result)

        return results

    # Отримати список контактів з днями народженнями
    def get_birthdays(self, days=30):
        today = datetime.date.today()
        upcoming_birthdays = []
        for contact in self.records:
            if contact.birthday:
                birthday = datetime.datetime.strptime(
                    contact.birthday, '%m/%d/%Y').date()
                if birthday.replace(year=today.year) < today:
                    birthday = birthday.replace(year=today.year + 1)
                if birthday <= today + datetime.timedelta(days=days):
                    upcoming_birthdays.append((contact.name, birthday))
        return upcoming_birthdays


address_book = AddressBook()

while True:
    print("Select an option:")
    print("1. Add contact")
    print("2. Edit contact")
    print("3. Delete contact")
    print("4. Search contact")
    print("5. View contacts")
    print("6. Search contact's birthdays")
    print("7. Exit")

    choice = input("> ")

    # Опція 1: додати новий контакт
    if choice == '1':
        name = input('Enter name: ')
        address = input('Enter address: ')
        phone = input('Enter phone number (format: xxx-xxx-xxxx): ')
        while not address_book.validate_phone_number(phone):
            print('Invalid phone number. Please enter again.')
            phone = input(
                'Enter phone number (format: xxx-xxx-xxxx): ')
        email = input('Enter email: ')
        while not address_book.validate_email(email):
            print('Invalid email. Please enter again.')
            email = input('Enter email: ')
        birthday = input('Enter birthday (format: mm/dd/yyyy): ')
        address_book.add(Record(name, address, phone, email, birthday))
        print('Contact added.')

    # Опція 2: редагувати існуючий контакт
    elif choice == '2':
        index = int(input('Enter the index of the contact to edit: '))
        contact = address_book.records[index]
        name = input(f'Enter name ({contact.name}): ')
        address = input(f'Enter address ({contact.address}): ')
        phone = input(f'Enter phone number ({contact.phone}): ')
        while not address_book.validate_phone_number(phone):
            print('Invalid phone number. Please enter again.')
            phone = input(f'Enter phone number ({contact.phone}): ')
        email = input(f'Enter email ({contact.email}): ')
        while not address_book.validate_email(email):
            print('Invalid email. Please enter again.')
            email = input(f'Enter email: ')
        birthday = input(
            f'Enter birthday ({contact.birthday}, format: mm/dd/yyyy): ')
        address_book.edit_contact(index, Record(
            name, address, phone, email, birthday))
        print('Contact edited.')

    # Опція 3: видалити контакт
    elif choice == '3':
        index = int(
            input('Enter the index of the contact to delete: '))
        address_book.delete_contact(index)
        print('Contact deleted.')

    # Опція 4: пошук контактів
    elif choice == '4':
        #search_term = input('Enter search term: ')
        results = address_book.search_contacts()
        print(f'Search results ({len(results)}):')
        for result in results:
            print(result)

    # Опція 5: вивести список всіх контактів
    elif choice == '5':
        print('Contacts:')
        for contact in address_book.records:
            print(contact)

    # Опція 6: вивести список контактів по дням народження
    elif choice == '6':
        days = int(
            input('Enter number of days to check for upcoming birthdays: '))
        upcoming_birthdays = address_book.get_birthdays(days)
        if not upcoming_birthdays:
            print('No upcoming birthdays.')
        else:
            print(f'Upcoming birthdays in the next {days} days:')
            for contact in upcoming_birthdays:
                print(contact)

    # Вихід
    elif choice == '7':
        address_book._save()
        print('Exit...')
        break
