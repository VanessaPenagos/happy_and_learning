class Lamp:
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self,_is_turn_on):
        self._is_turn_on = _is_turn_on

    def turn_on(self):
        self._is_turn_on = True
        self._display_image()

    def turn_off(self):
        self._is_turn_on = False
        self._display_image()

    def _display_image(self):
        if self._is_turn_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

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
