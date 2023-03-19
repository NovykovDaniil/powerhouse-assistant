from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

html_completer = WordCompleter(['<html>', '<body>', '<head>', '<title>'])
#text = prompt('Enter HTML: ', completer=html_completer)
#print('You said: %s' % text)

a = ''''Add' : 'add contact',
            'Search' : 'search contact using any information',
            'Edit' : 'edit recorded contact',
            'Delete' : 'delete existing contact',
            'Save' : 'save your contact book to the file',
            'Load' : 'recover contacts from the file',
            'Congratulate' : 'find out who you need to congratulate in the near future',
            'Show'''

print(a.split(':')[::3])
