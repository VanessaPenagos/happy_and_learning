def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

lst = [1, 2, 2, 3, 4, 4, 5]
unique = remove_duplicates(lst)
print("Unique elements:", unique)
