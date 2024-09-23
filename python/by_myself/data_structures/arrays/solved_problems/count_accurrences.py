def count_name(names, name_to_count):
    count = names.count(name_to_count)
    return count

names = ["John", "Maria", "John", "Peter", "Maria"]
count = count_name(names, "John")
print("The name 'John' appears:", count, "times.")
