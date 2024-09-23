# -*- coding: utf-8 -*-

def protected(func):
    def wrapper(password):
        if password == 'vanessa':
            return func()
        else:
            print('Your password is wrong!')
    return wrapper

@protected
def protected_func():
    print('Your password is correct!')

if __name__ == '__main__':
    password = str(input('Enter your password: '))
    protected_func(password)
