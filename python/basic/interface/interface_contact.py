# -*- coding: utf-8 -*-


class Contact:

    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email


class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        print('name: {}, phone: {}, email: {}'.format(name, phone, email))

def run():
    contact_book = ContactBook()

    while True:
        command = str(input('''
            What do you want to do?

            [a]add contact
            [u]pdate contact
            [s]earch contact
            [d]elete contact
            [l]ist contacts
            [e]xit
        '''))

        if command == 'a':
            name = str(input('Write the contact name: '))
            phone = str(input('Write the contacts phone number: '))
            email = str(input('Write the contact email: '))

            contact_book.add(name, phone, email)

        elif command == 'u':
            print('update contact')

        elif command == 's':
            print('search contact')

        elif command == 'd':
            print('delete contact')

        elif command == 'l':
            print('list contacts')

        elif command == 'e':
            break
        else:
            print('Command not found.')

if __name__ == '__main__':
    run()
