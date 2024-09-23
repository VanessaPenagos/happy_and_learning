def filter_even(numbers):
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    return evens

numbers = [1, 2, 3, 4, 5, 6]
evens = filter_even(numbers)
print("Even numbers:", evens)
