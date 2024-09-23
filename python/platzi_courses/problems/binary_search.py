# -*- coding: utf-8 -*-
def binary_search(numbers, number_to_find, low, high):
    if low > high:
        return False

    mid = (low + high) / 2
    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, high - 1)

if __name__ == '__main__':
    numbers = [1,2,5,6,9,10,12,15,17,25,69,78]
    numer_to_find = int(raw_input('Enter the number: '))

    result = binary_search(numbers, numer_to_find, 0, len(numbers) - 1)

    if result == True:
        print('The number is in the list!')
    else:
        print('The number is not in the list!')
