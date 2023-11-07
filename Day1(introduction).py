# Introduction
# Day 1 - 30DaysofPython Challenge by Swift Cyberwatch
# SIMPLE OPERATIONS
print(2 + 3)   # Addition(+)
print(3 - 1)   # Subtraction(-)
print(2 * 3)   # Multiplication(*)
print(3 / 2)   # Division(/)
print(3 ** 2)  # Exponential(**)
print(3 % 2)   # Modulus(%)
print(3 // 2)  # Floor Division operator(//)


# DATA TYPES

# WHAT IS DAtA TYPE?
'''
A data type is a classification that specifies which type of value a variable or expression 
can hold in a programming language. It defines the characteristics of the data, including
the range of values it can take, the operationshat can be performed on it, and how the data is stored in memory.
'''
print(type(10))        # Int is short for integer. It is a datatype that represents whoe numbers e.g 3, 4 and -1 e.t.c
print(type(3.14))      # Float repereesents numbers with decimal points, like 3.14.
print(type(1 + 3j))    # Complex represents complex numbers with real and imaginary parts, like 2 + 3j
print(type('Asabeneh'))# String represents text or sequences of characters like "Hello, world"
print(type([1, 2 , 3]))# List represents ordered collections of items, like [1, 2 ,3]
print(type({'name' : 'Joules'}))# Dictionaries represent collections of key-value pairs,
                                 # like {'name' : 'Joules', 'sex' : 'Male'}
print(type({9.8, 3.14, 2.7})) # Set represents unordderd collections of uniqu elements, like {1, 2, 3}
print(type((9.8, 3.14, 2.7))) # Tuple represents ordered colletions, like (1, 2, 3), but immutabe.