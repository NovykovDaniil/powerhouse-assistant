from Note import *
from abc import ABC, abstractmethod
import re
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit import prompt


class NoteBot:
    def __init__(self) -> None:
        self.note_book = NoteBook()


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
        return note_instance.note_book.add_note(input("Note text: "))


class ShowAll(Command):
    def processing(self, note_instance: NoteBot):
        return note_instance.note_book.show_all()


class FindNote(Command):
    def processing(self, note_instance: NoteBot):
        subtext = input("Enter subtext to find contact: ")
        return note_instance.note_book.find_note(subtext)


class AddDate(Command):
    def processing(self, note_instance: NoteBot):
        id = int(prompt('Give an id: ', validator=ValidateID()))
        date = prompt('Date: ', validator=ValidateDate())
        return note_instance.note_book.add_date(id, date)


class ChangeNote(Command):
    def processing(self, note_instance: NoteBot):
        id = int(prompt('Give an id: ', validator = ValidateID()))
        return note_instance.note_book.change_note(id, input("Enter new note: "))


class DelNote(Command):
    def processing(self, note_instance: NoteBot):
        id = int(prompt('Give an id: ', validator = ValidateID()))
        return note_instance.note_book.del_note(id)


class ShowDate(Command):
    def processing(self, note_instance: NoteBot):
        date = prompt('Date: ', validator = ValidateDate())
        days = int(prompt('Days range (optionally): ', validator = ValidateDays()))
        return note_instance.note_book.show_date(date, days)


class DoneNote(Command):
    def processing(self, note_instance: NoteBot):
        id = int(prompt('Give an id: ', validator=ValidateID()))
        return note_instance.note_book.done_note(id)


class ReturnNote(Command):
    def processing(self, note_instance: NoteBot):
        id = int(prompt('Give an id: ', validator=ValidateID()))
        return note_instance.note_book.return_note(id)


class AddTag(Command):
    def processing(self, note_instance: NoteBot):
        id = int(prompt('Give an id: ', validator=ValidateID()))
        return note_instance.note_book.add_tag(id, input("Enter tags: "))


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


class ValidateID(Validator):
    def validate(self, document) -> None:
        id = document.text
        if not id.isdigit():
            i = 0
            for i, c in enumerate(id):
                if not c.isdigit():
                    break
            raise ValidationError(message='ID should be an integer', cursor_position=i)


class ValidateDate(Validator):
    def validate(self, document) -> None:
        date = document.text
        if not re.match(r"\d{2}[.]\d{2}[.]\d{4}", date):
            raise ValidationError(message='Data should be in format day.month.year', cursor_position = 0)
        

class ValidateDays(Validator):
    def validate(self, document) -> None:
        days = document.text
        if not days.isdigit():
          days = 0
          raise ValidationError(message='Days should be an integer', cursor_position = 0)  


def get_handler(action):
    for command_container in COMMANDS.keys():
        for command in command_container:
            if action in command:
                return COMMANDS[command_container]()


def performer(command: Command, note_instance: NoteBot):
    return command.processing(note_instance)



nb = NoteBot()
while True:
    act = input('command: ')
    if act == 'exit':
        break
    try:
        print(performer(get_handler(act), nb))
    except:
        print('no command')
    
