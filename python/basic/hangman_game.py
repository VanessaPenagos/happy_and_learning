# -*- coding: utf-8 -*-
import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = ['bts',
        'namjoon',
        'seokjin',
        'yoongi',
        'hoseok',
        'jimin',
        'taehyung',
        'jungkook',
        'persona',
        'love',
        'yourself'
]

def random_word():
    idx = random.randint(0, len(WORDS)- 1)
    return WORDS[idx]

def display_board(hidden_word,tries):
    print(IMAGES[tries])
    print('')
    print('  '.join(hidden_word))
    print(' ')
    print('**************************************************')

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word,tries)
        current_letter = str(raw_input('Choose a letter: '))

        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)

        if len(letter_indexes) == 0:
            tries += 1

        if tries == 7:
            display_board(hidden_word,tries)
            print(' ')
            print('You lost! The correct word was: {}'.format(word))
            break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []

if __name__ == '__main__':
    print('')
    print('A R M Y    H A N G M A N   G A M E')
    run()
