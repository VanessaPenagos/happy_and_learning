#from the basic platzi course

"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def character_not_repeated(char_sequence):
    seen_letters = {}
    for index, letter in enumerate(char_sequence):
        #if letter in seen_letters:
        if letter not in seen_letters:
            seen_letters[letter] = (index,1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

        final_letters = []
        for key, value in seen_letters.iteritems():
            if value[1] = 1
            final_letters.append((key,value[0]))

        not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

        if not_repeated_letters:
            return not_repeated_letters
        else:
            return '_'


if __name__ == '__main__':
    char_sequence = str(raw_input('Write a sequence of characters: '))

    result = character_not_repeated(char_sequence)

    if result == '_':
        print('All characters are repeated.')
    else:
        print('The first character not repeated is: {}'.format(result))
