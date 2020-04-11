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
        contact = Contact(name,phone,email)
        self._contacts.append(contact)

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self,name):
        for idx, contact in enumerate(self._contacts):
            if contact._name.lower() == name.lower():
                del self._contacts[idx]
                break
        else:
            print('contact not found!')

    def search(self,name):
        for contact in self._contacts:
            if contact._name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            print('contact not found!')

    def _print_contact(self, contact):
        print('----------------------------------')
        print('Name: {}'.format(contact._name))
        print('Number: {}'.format(contact._phone))
        print('Email: {}'.format(contact._email))
        print('----------------------------------')

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
            name = str(input('Write the contact name: '))
            contact_book.search(name)

        elif command == 'd':
            name = str(input('Write the contact name: '))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 'e':
            break
        else:
            print('Command not found.')

if __name__ == '__main__':
    run()
