# # def validate_mobile_number(input_value):
# #     input_value = int('mobile_number')
# #     if type('mobile_number') == int:
# #         return 'You have been logged in.'
# #     else:
# #         return 'Invalid Input'

# user_input = input('Enter your mobile number: ')
# if type('mobile_number') == int:
#     print('You have been logged in.')
# else:
#     print('Invalid Input')
# # output = validate_mobile_number(user_input)
# # print(output)

mobile_number = input('Enter your mobile number: ')
if mobile_number.isdigit():
    print('You have been logged in')
else:
    print('Invalid input')

import numpy as np
import numpy as np

x = np.random.random()

result = np.sin(x)**2 + np.cos(x)**2

result_defined = np.round(result, 0)
print(result_defined)

