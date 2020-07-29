# -*- coding: utf-8 -*-

from lamp import Lamp

def run():
    lamp = Lamp(_is_turn_on=False)

    while True:
        command = str(input('''
    choose an option
        1. turn on
        2. to turn off
        3. exit

        '''))

        if command == '1':
            lamp.turn_on()
        elif command == '2':
            lamp.turn_off()
        else:
            break

if __name__ == '__main__':
    run()
