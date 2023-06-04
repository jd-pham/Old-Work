'''
Name: James Pham
Date: 2/3/2023
Class: DSC1302


'''
def is_vowel(char):
    vowels = {'a', 'e','i','o','u'}
    if len(char) > 1:
        print('Value is not a character')
        return False
    if char.lower() in vowels:
        return True
    return False

print('Q1: ----------------------------------------------------')
character = 'A'
res = is_vowel(character)
print(character, res)

character = 'b'
res = is_vowel(character)
print(character, res)


print('Q2------------------------------------------')
def divisibles_5():
    for i in range(0,101,5):
        if i == 0:
            continue
        print(i)
divisibles_5()


print('Q3-----------------------------------------')
def in_order(integer_list: list):
    sorted_list = []
    for ele in integer_list:
        sorted_list.append(ele)
    
    max = integer_list[0]
    for ele in integer_list[1:]:
        if ele < max:
            print('Not in order')
            return False
        max = ele
    print('In order')
    return True
    

input_list = [3,2,1]
res = in_order(input_list)
print(res, input_list, '\n')

input_list = [1,2,3]
res = in_order(input_list)
print(res, input_list)

print()
input_list = [2,1,3]
res = in_order(input_list)
print(res, input_list)

