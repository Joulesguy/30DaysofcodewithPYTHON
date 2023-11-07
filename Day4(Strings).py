# Day 4 - 30Daysofython Challenge with Swift Cyberwatch

# Single line comment
# A string could be a single character or a bunch of texts
letter = 'PYTHON'
print("Length of the 'letter' variable: ", len(letter))
greeting = 'Hello, world!'   # String could be a single or double quote"Hello world!"
print(greeting)       # Hello world
print(len(greeting))  # 13
sentence = "I hope you're enjoying 30 days of python challenge"
print(sentence)

# Multiline string
multiline_string = '''I am a teacher and I enjoy teaching.
I don't find anything as rewarding as teaching people.
That's why I started 30 days of python.'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am a teacher and I enjoy teaching.
I don't find anything as rewarding as teaching people.
That's why I started 30 days of python."""
print(multiline_string)

# String Concatenation
first_name = 'Joules'
last_name = 'Pentazocine'
space = ' '
full_name = first_name + space + last_name
print(full_name)    # Joules Pentazocine
# Checking length of a string using len() builtin function
print(len(first_name))   # 6
print(len(last_name))    # 11
print(len(first_name) > len(last_name))  # False
print(len(full_name))  # 18

### Unpacking characters
language = 'Python'
a,b,c,d,e,f = language
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# Accessing characters in string by index
language = 'Python'
first_letter = language[0]
print(first_letter)  # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)   # n

# If we want to start from right end, we can use negative indexing. -1 is the last index.
language = 'Python'
last_letter = language[-1]
print(last_letter)  # n
second_last = language[-2]
print(second_last)  # o

# Slicing

language = 'Python'
first_three = language[0:3]  # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three)  # hon

# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Skipping character while splitting python strings
language = 'Python'
pto = language[0:6:2]
print(pto)  # pto


# Escape sequence
print('I hope everyone is enjoying the python challenge. \nDo you?')   # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('This is a back slash symbol (\\)')  # To write a back slash
print('In every programming language, it starts with \"Hello world"')

# Strings Methods
# capitalize(: Converts the first character, the string to Capital letter)
challenge = 'thirty days of python'
print(challenge.capitalize())  # Thirty days of python

# #count(): returns occurences of substring in string, count(substring, start = ..., end=...)

challenge = 'thirty days of python'
print(challenge.count('y'))  # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th'))  # 2

# # endswith(): Checks if a string ends ith a specified ending

# challenge = 'thirty days of python'
print(challenge.endswith('on'))     # True
print(challenge.endswith('tion'))   # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())     # thirty  days    of      python
print(challenge.expandtabs(10))   # thirty    days      of        python

# find(): Returns the index of first occurence of substring
challenge = 'thirty days of python'
print(challenge.find('y'))   # 5
print(challenge.find('th'))  # 0

# Format() formats string into nicer output
first_name = "Joules"
last_name = 'Pentazocine'
job = 'Pharmacist'
country = 'Naija'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence)   # I am Joules Pentazocine. I am a Pharmacist. I live in Naija.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result)   # The area of circle with 10 is 314.0

# index(): Returns the index of substring
challenge = 'thirty days of python'
print(challenge.index('y'))  # 5
print(challenge.find('th'))  # 0

# # isalnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())   # True

challenge = '30DaysPython'
print(challenge.isalnum())   # True

challenge = 'thirty days of python'
print(challenge.isalnum())   # False

challenge = 'thirty days of python 2019'
print(challenge.isalnum())  # False

# # isalpha(): Checks if all characters are alphabets

challenge = 'thirtydaysofpython'
print(challenge.isalpha())  # True
num = '123'
print(num.isalpha())   # False

# isdigit(): Checks Digit Characters

challenge = 'Thirty'
print(challenge.isdigit())   # False
challenge = '30'
print(challenge.isdigit())    # True

# # isdecimal(): Checks Decimal characters

num = '10'
print(num.isdecimal())   # True
num = '10.5'
print(num.isdecimal())   # False


# # isidentifier(): checks for valid idebtifier means it checks if a string is a valid variable name
challenge = '30DaysofPython'
print(challenge.isidentifier())  # False because it starts with a number
chalenge = 'thirty_days_of_python'
print(challenge.isidentifier())    # True

# islower(): checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower())   # True
challenge = 'Thirty days of python'
print(challenge.islower())   # False

# isupper(): returns if all characters are uppercase characters

challenge = 'thirty days of python'
print(challenge.isupper())  # False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())   # True

# isnumeric(): Checks numeric characters

num = '10'
print(num.isnumeric())   # True
print('ten'.isnumeric()) # False

# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JAVASCRIPT', 'REACT']
result = '#, '.join(web_tech)
print(result)   # HTML#, CSS#, JAVASCRIPT#, REACT

# strip(): removes both leading and trailing characters

challenge = ' thirty days of python '
print(challenge.strip('y'))  # 5

# replace(): replaces substring inside
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))    # thirty days of coding

#plit(): Splits string from the left
challenge = 'thirty days of python'
print(challenge.split())   #['thirty', 'days', 'of', 'python']

# title(): Returns a Title cased string
challenge = 'thirty days of python'
print(challenge.title())   # Thirty Days Of Python

# swapcase(): Checks if string starts with the specified string

challenge = 'thirty days of python'
print(challenge.swapcase())  # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String starts with the specified string

challenge = 'thirty days of python'
print(challenge.startswith('thirty'))  # True
challenge = '30 days of python'
print(challenge.startswith('thirty'))  # False