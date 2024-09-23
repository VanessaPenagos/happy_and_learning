def square_list(numbers):
    squares = [number ** 2 for number in numbers]
    return squares

numbers = [1, 2, 3, 4, 5]
squares = square_list(numbers)
print("Squares:", squares)
