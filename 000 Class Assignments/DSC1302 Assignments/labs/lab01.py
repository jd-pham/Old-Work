'''
Name: James Pham
Date: 01/20/23
Class: DSC1302

'''


user_input = input('Please input a first name, generic location, integer, and plural object, each separated by a comma.\n')

user_input = user_input.split(',')
if len(user_input) != 4:
    print("Incorrect inputs")
    exit()
    
print(user_input)
name = user_input[0]
location = user_input[1]
count = user_input[2]
item = user_input[3]
print(f'{name} went to {location} and bought {count} {item} while they were there.')


