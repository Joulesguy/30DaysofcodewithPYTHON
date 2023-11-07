# Variables in Python
# Day 2 - 30DaysofPython Challenge by Swift Cyberwatch

# What are variables?

first_name = 'Joules'
last_name = 'Pentazocine'
country = 'Naija'
city = 'Ilorin'
age = 100
is_single = True
skills = ['HTML', 'small CSS', 'Excel', 'Python']

person_info = {
        'first_name' : 'Joules',
        'last_name' : 'Pentazocine',
        'country' : 'Naija',
        'city' : 'Ilorin'
        }

# Printing the values stored in the variables

print('First_name: ', first_name)
print('First name length: ', len(first_name))    # The function len shows the length of the character
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('Age: ', age)
print('Is single: ', is_single)
print('Skills: ', skills)
print('Person Information: ', person_info)


# Declaring multiple variables in one line

first_name, last_name, country, age, is_single = 'Joules', 'Pentazocine', 'Naija', 100, True

print(first_name, last_name, country, age, is_single)
print('First_name: ', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Is single: ', is_single)