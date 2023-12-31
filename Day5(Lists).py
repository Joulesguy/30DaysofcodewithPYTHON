# Day 5 - #30DaysOf Python Challenge by Swift Cyberwatch
 
empty_list = list() # This is an empy list, no item in he list
print(len(empty_list))

fruits = ['banana', 'orange', 'mango', 'lemon']  # List of fruits
vegetables = ['Tomato','Potato', 'Cabbage', 'Onion', 'Carrot']  # List of vegetables
animal_products = ['milk','meat', 'butter', 'yoghurt']   # List of animal products
web_techs = ['HTML','CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']  # List ofweb technologies
countries = ['Finland', 'Estonia','Denmark', 'Sweden', 'Norway']

# Print the lists and its length
print('Fruits: ', fruits)
print('NUmberof Fruits: ',len(fruits))
print('Vegetables: ',vegetables)
print('Numberof Vegetables: ',len(vegetables))
print('Animal products: ', animal_products)
print('Number of Animal Products: ', len(animal_products))
print('Web Tech: ', web_techs)
print('Numberof Web Tech: ', len(web_techs))
print('Countries: ', countries)
print('Number of Countries: ', len(countries))


# Modifying list
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]  # we are accessing the first item using it's index
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)  # orange
last_fruit = fruits[3]
print(last_fruit)  # lemon

# lastindex
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Accessing items
fruits = ['banana', 'orange', 'mango', 'lemon']
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)   # lemon
print(second_last)   # mango


# Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]   # It returns all the fruits
# this also gives the same result as the above
all_fruits = fruits[0:]   # If we don't set where to stop, it takes all the rest
orange_and_mango = fruits[1:3]  # It does not include the end index
orange_mango_lemon = fruits[1:]

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
# this also gives the same result as the above
orange_and_mango = fruits[-3:-1] # it does not include the last index
orange_mango_lemon = fruits[-3:]

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'Avocado'
print(fruits)    # ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'Apple'
print(fruits)   # ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)  # ['Avocado', 'Apple', 'mango', 'lime']

# Checking items 
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist) # False

# Append
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)    # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   
print(fruits)   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']

# Insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')  # insert apple between orange and mango
print(fruits)    # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')  # inserts lime between apple and mango
print(fruits)   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']

# Remove
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits) # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']

# pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)  # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)   # ['orange', 'mango']

# Del   It always accepts an input
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits)  # ['orange', 'mango', 'lemon']

del fruits[1]
print(fruits)  # ['orange', 'lemon']
del fruits
print(fruits)  # This should give: NameError: name 'fruits' is not defined

# clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)  # []

# copying a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)   #  ['banana', 'orange', 'mango', 'lemon']


# Join
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers 
print(integers)   # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato','Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# join with extend
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers: ', num1)
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers: ', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato','Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and Vegetables: ', fruits)

# count  Returns number of occurences of a value
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))  # 3

# index
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))  # 2

# Reverse  reverses the order in which the list is arranged
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()  
print(fruits)      
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

# sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse = True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse = True)
print(ages)