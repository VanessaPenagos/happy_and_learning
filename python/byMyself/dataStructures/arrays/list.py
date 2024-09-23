#Empty list
my_list = []

#With elements  
numbers_list = [1,2,3,4,5,6]
words_list = ["a", "b", "c", "d"]

#get elements from a list
first_number = numbers_list[0]    

#update elements 
words_list[1] = "f"

#add or remove elements from a list
numbers_list.remove(3)
words_list.append("w")

#list length
len(words_list)
len(numbers_list)

#iterate a list
for number in numbers_list:
    print(number)
