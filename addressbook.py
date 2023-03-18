import datetime
import pickle
import logging
import os
from prettytable import PrettyTable
from addressbook_data import *

logger = logging.getLogger("ab_log")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("[%(asctime)s]   %(message)s")
fh = logging.FileHandler("logs\\address_book.log")
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(fh)


class AddressBook:
    def __init__(self):
        self.data = []
        logger.info("Address book has been created")

    def add(self, record):
        self.data.append(
            {
                "Name": record.name,
                "Phone": record.phone,
                "Address": record.birthday,
                "Email": record.email,
                "Birthday": record.address,
            }
        )
        logger.info("The contact has been recorded successfully")
        return "The contact has been recorded successfully"

    def save(self, path):
        path = path + ".bin" if not path.endswith(".bin") else path
        with open(path, "wb") as fd:
            pickle.dump(self.data, fd)
            logger.info(f"Address Book has been saved to {path}")
            return f"Address Book has been saved to {path}"

    def load(self, path):
        try:
            path = path + ".bin" if not path.endswith(".bin") else path
            with open(path, "rb") as fd:
                if not os.stat(path).st_size == 0:
                    self.data = pickle.load(fd)
                    logger.info(f"Address Book has been loaded from {path}")
                    return f"Address Book has been loaded from {path}"
                logger.info(f"File to load is empty")
                return "File to restore is empty"
        except FileNotFoundError:
            return "There is no such file!"

    @staticmethod
    def table_filler(table, contact):
        table.field_names = ["Name", "Phone", "Address", "Email", "Birthday"]
        phone_to_show = (
            " +".join(contact["Phone"].split("+")) if contact["Phone"] else ""
        )
        birthday_to_show = (
            contact["Birthday"].date()
            if not isinstance(contact["Birthday"], str)
            else contact["Birthday"]
        )
        table.add_row(
            [
                contact["Name"],
                phone_to_show,
                contact["Address"],
                contact["Email"],
                birthday_to_show,
            ]
        )

    def show(self):
        table = PrettyTable()
        for contact in self.data:
            self.table_filler(table, contact)
        return table

    def edit(self, contact_data, new_category):
        category_container = {
            "Name": Name,
            "Phone": Phone,
            "Email": Email,
            "Address": Address,
            "Birthday": Birthday,
        }
        result = [
            contact
            for contact in self.data
            for val in contact.values()
            if str(contact_data).lower().strip() in str(val).lower().strip()
        ]
        if not result:
            return "There is no such contact"
        try:
            if new_category not in category_container.keys():
                raise ValueError
            else:
                result[0][new_category] = category_container[new_category]().value
                current_contact_name = result[0]["Name"]
                logger.info(f"Contact {current_contact_name} has been edited ")
                return f"Contact {current_contact_name} has been edited "
        except ValueError:
            return "There is no such category"

    def delete(self, contact_info_to_remove):
        try:
            contact_to_remove = [
                i
                for i in self.data
                for info in i.values()
                if contact_info_to_remove in info.strip().lower()
            ]
            self.data.remove(contact_to_remove[0])
            current_contact_name = contact_to_remove[0]["Name"]
            logger.info(f"Contact {current_contact_name} has been deleted")
        except IndexError:
            print("There is no such contact!")

    def search(self, category, search_parameter):
        matching_contacts = []
        available_categories = [
            "name",
            "phone",
            "email",
            "address",
            "birthday",
        ]
        if category not in available_categories:
            return "There is no such category"
        for contact in self.data:
            if search_parameter in contact[category.capitalize()].lower():
                matching_contacts.append(contact)
            else:
                return "There is no such contact"

        if matching_contacts:
            table = PrettyTable()
            for contact in matching_contacts:
                self.table_filler(table, contact)
        return table

    def congratulate(self, days_range):
        start_date = datetime.datetime.now() + datetime.timedelta(days=1)
        stop_date = start_date + datetime.timedelta(days=days_range)
        congratulate_dict = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
            "Saturday": [],
            "Sunday": [],
        }
        for contact in self.data:
            if contact["Birthday"]:
                if contact["Birthday"] > stop_date:
                    continue
                current_birthday = contact["Birthday"].replace(year=datetime.datetime.now().year)
                if current_birthday < start_date:
                    current_birthday += datetime.timedelta(days=365)
                if start_date < current_birthday < stop_date:
                    congratulate_dict[current_birthday.strftime("%A")].append(contact["Name"])

        table = PrettyTable()
        table.field_names = ['Weekday', 'Сelebrants']
        for weekday, celebrants in congratulate_dict.items():
            table.add_row([weekday, ' '.join(celebrants)])
        return table