def sum_list(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

numbers = [1, 2, 3, 4, 5]
result = sum_list(numbers)
print("The sum is:", result)