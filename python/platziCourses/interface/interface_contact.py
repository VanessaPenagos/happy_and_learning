# -*- coding: utf-8 -*-
import csv

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
        self._save_contacts()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self,name):
        for idx, contact in enumerate(self._contacts):
            if contact._name.lower() == name.lower():
                del self._contacts[idx]
                self._save_contacts()
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

    def _save_contacts(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))
            for contact in self._contacts:
                writer.writerow((contact._name,contact._phone,contact._email))

    def _print_contact(self, contact):
        print('----------------------------------')
        print('Name: {}'.format(contact._name))
        print('Number: {}'.format(contact._phone))
        print('Email: {}'.format(contact._email))
        print('----------------------------------')

def run():
    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0 or not row:
                continue
            contact_book.add(row[0],row[1],row[2])

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
