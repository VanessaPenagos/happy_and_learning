def find_max_min(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    return maximum, minimum

numbers = [10, 5, 3, 8, 15]
maximum, minimum = find_max_min(numbers)
print("Maximum:", maximum, "Minimum:", minimum)
