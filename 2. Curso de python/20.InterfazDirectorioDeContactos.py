# -*- coding: utf-8 -*-
import csv

class ContactBook:
    def __init__(self):
        self._contacts = []
    def add(self,name,phone,email):
        contact = Contact(name,phone,email)
        self._contacts.append(contact)
        self._save()
    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)
    def delete(self,name):
        for idx,contact in enumerate(self._contacts):
            if contact._name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break
    def search(self,name):
        for contact in self._contacts:
            if contact._name.lower() == name.lower():
                self._print_contact(contact)
    def update(self,name):
        for contact in self._contacts:
            if contact._name.lower() == name.lower():
                option = str(input('''
                Que dato desea actualizar:
                [n]ombre
                [e]mail
                [t]eléfono
                '''))
                if option == 'n':
                    contact._name = str(input('Nombre: '))
                elif option == 'e':
                    contact._email = str(input('Email: '))
                elif option == 't':
                    contact._phone = str(input('Teléfono: '))
                else:
                    print('***       Comando no encontrado       ***')
                return
        self._not_found()

    def _save(self):
        with open('contacts.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone', 'email'))
            for contact in self._contacts:
                writer.writerow((contact._name, contact._phone, contact._email))

    def _print_contact(self,contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact._name))
        print('Telefono: {}'.format(contact._phone))
        print('Email: {}'.format(contact._email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')
    def _not_found(self):
        print('***********')
        print('No encontado!!!')
        print('***********')

class Contact:
    def __init__(self,name,phone,email):
        self._name = name
        self._phone = phone
        self._email = email

def run():

    contact_book = ContactBook()

    try:
        with open('contacts.csv','r') as f:
            reader = csv.reader(f)
            for idx,row in enumerate(reader):
                if row:
                    if idx == 0:
                        continue
                    contact_book.add(row[0],row[1],row[2])
    except FileNotFoundError:
        print('No se encontró el archivo contacts.cvs')

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]Ã±adir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el telefono del contacto: '))
            email = str(input('Escribe el email del contacto: '))
            contact_book.add(name,phone,email)

        elif command == 'ac':
            name = str(input('Escriba el nombre del contacto: '))
            contact_book.update(name)

        elif command == 'b':
            name = str(input('Escriba el nombre del contacto: '))
            contact_book.search(name)

        elif command == 'e':
            name = str(input('Escriba el nombre del contacto: '))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    run()
