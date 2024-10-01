#two ways to creat a set 
fruits = {"apple", "banana", "lemon"}
numbers = set([1,2,3,4,5])

#Basic operations 
fruits.add("avocado")
fruits.remove("apple")
len(fruits)
print("banana" in fruits)   # check if an element is in a set

#Set operations

set_a = {'a', 'b', 'c'}
set_b = {'c', 'd', 'e'}

#Union
union_set = set_a | set_b 
#Intersection 
intersection_set = set_a & set_b
#Diference
diference_set = set_a - set_b
#Symetric diference
symetric_diference = set_a ^ set_b