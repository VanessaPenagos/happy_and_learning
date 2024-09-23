# -*- coding: utf-8 -*-

# print(f.readlines())
def run():
    counter = 0
    with open('pied_piper.txt') as f:
        for line in f:
            counter += line.count('Hamelin')
    print('Hamelin is {} in the tale'.format(counter))


if __name__ == '__main__':
    run()
