from Note import *
from abc import ABC, abstractmethod
import re


class NoteBot:
    def __init__(self) -> None:
        self.note_book = NoteBook("notes.dat")


class Command(ABC):
    @abstractmethod
    def processing(self, note_instance: NoteBot):
        pass


class HelpMe(Command):
    def processing(self, note_instance: NoteBot):
        return note_instance.note_book.help_me()


class GoodBye(Command):
    def processing(self, note_instance: NoteBot):
        return note_instance.note_book.goodbye()


class AddNote(Command):
    def processing(self, note_instance: NoteBot):
        note_text = input("Note text: ")
        return note_instance.note_book.add_note(note_text)


class ShowAll(Command):
    def processing(self, note_instance: NoteBot):
        return note_instance.note_book.show_all()


class FindNote(Command):
    def processing(self, note_instance: NoteBot):
        subtext = input("Enter subtext to find contact: ")
        return note_instance.note_book.find_note(subtext)


class AddDate(Command):
    def processing(self, note_instance: NoteBot):
        return note_instance.note_book.add_date(input_id(), input_date())


class ChangeNote(Command):
    def processing(self, note_instance: NoteBot):
        return note_instance.note_book.change_note(
            input_id(), input("Enter new note: ")
        )


class DelNote(Command):
    def processing(self, note_instance: NoteBot):
        return note_instance.note_book.del_note(input_id())


class ShowDate(Command):
    def processing(self, note_instance: NoteBot):
        return note_instance.note_book.show_date(input_date(), input_days())


class DoneNote(Command):
    def processing(self, note_instance: NoteBot):
        return note_instance.note_book.done_note(input_id())


class ReturnNote(Command):
    def processing(self, note_instance: NoteBot):
        return note_instance.note_book.return_note(input_id())


class AddTag(Command):
    def processing(self, note_instance: NoteBot):
        return note_instance.note_book.add_tag(input_id(), input("Enter tags: "))


COMMANDS = {
    ("?", "help", "h"): HelpMe,
    ("buy", "good bye", "close", "exit", "."): GoodBye,
    ("add note ", "+", "new "): AddNote,
    ("add date",): AddDate,
    ("show all",): ShowAll,
    ("change note ",): ChangeNote,
    ("delete note ", "remove note", "del note"): DelNote,
    ("find note ", "find ", "search "): FindNote,
    ("show date ",): ShowDate,
    ("done ",): DoneNote,
    ("return",): ReturnNote,
    ("add tag",): AddTag,
}


def input_id():
    while True:
        try:
            id_contact = int(input("Contact ID: "))
            break
        except ValueError:
            print("ID should be an integer")
    return id_contact


def input_date():
    while True:
        date = input("Date (day.month.year): ")
        if re.match(r"\d{2}[.]\d{2}[.]\d{4}", date):
            break
        else:
            print("Data should be in format day.month.year")
    return date


def input_days():
    days = input("Days range(optionally): ")
    if days.isalnum():
        days = int(days)
    else:
        print("Days should be an integer")
        days = 0
    return days


def get_handler(action):
    for command_container in COMMANDS.keys():
        for command in command_container:
            if action in command:
                return COMMANDS[command_container]()


def performer(command: Command, note_instance: NoteBot):
    return command.processing(note_instance)
