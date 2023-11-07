def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight

def sum_two_num (num1, num2):
    total = num1 + num2
    return total

def gravity (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight

def mean_numbers(first_num, arg):
    sum = str(first_num + arg)
    mean = sum / len(mean_numbers)
    return mean
print(mean_numbers(5, 6))