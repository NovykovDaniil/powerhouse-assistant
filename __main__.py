import AddressBook.Address_Book_Handler as abh
import NoteBook.Note_Book_Handler as nbh
from Sort_Files import *
from calculator import *
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

def calculator():
    return start_calc()

def folder_sorter():
    return start_sorting()

def address_book():
    address_container = abh.AddressBot()
    address_book_completer = WordCompleter(['help', 'add', 'search', 'edit', 'delete', 'save', 'load', 'congratulate', 'show'])
    print('You have entered the address book. Enter your command ("help" to get a description of the commands)')
    while True:
        action = prompt('>>> ', completer=address_book_completer)
        if action == 'exit': 
            break
        try:
            print(abh.performer(abh.get_handler(action), address_container))
        except:
            print('There is no such command')
    return 'Thank you for using our address book!'

def note_book():
    note_container = nbh.NoteBot()
    note_book_completer = WordCompleter(['help', 'add note', 'add date', 'show all', 'change note', 'delete note', 'search', 'show date', 'done', 'return', 'add tag', 'sort by tags'])
    print('You have entered the note book. Enter your command ("help" to get a description of the commands)')
    while True:
        action = prompt('>>> ', completer=note_book_completer)
        if action == 'exit':
            note_container.book.save()
            break
        try:
            print(nbh.performer(nbh.get_handler(action), note_container))
        except KeyError:
            print('There is no such command')
    return 'Thank you for using our address book!'


def main():

    print('''   _____                           _                             _       _                 _   
  / ____|                         | |           /\              (_)     | |               | |  
 | |      ___   _ __   ___   ___  | |  ___     /  \    ___  ___  _  ___ | |_  __ _  _ __  | |_ 
 | |     / _ \ | '_ \ / __| / _ \ | | / _ \   / /\ \  / __|/ __|| |/ __|| __|/ _` || '_ \ | __|
 | |____| (_) || | | |\__ \| (_) || ||  __/  / ____ \ \__ \\\\__ \| |\__ \| |_| (_| || | | || |_ 
  \_____|\___/ |_| |_||___/ \___/ |_| \___| /_/    \_\|___/|___/|_||___/ \__|\__,_||_| |_| \__|''')
    
    while True:
        main_completer = WordCompleter(['address book', 'note book', 'folder sorter', 'calculator', 'exit'])
        main_action = prompt('''You are in the main menu! Please select the section you need.\n> address book\n> note book\n> folder sorter\n> calculator\n> exit\n>>> ''', completer=main_completer)
        if main_action == 'exit': break
        handler = {'calculator' : calculator, 'folder sorter' : folder_sorter, 'address book' : address_book, 'note book' : note_book}
        try:
            print(handler[main_action]())
        except KeyError:
            print('There is no such command')

    return 'Thank you for using our concole assistant'

print(main())