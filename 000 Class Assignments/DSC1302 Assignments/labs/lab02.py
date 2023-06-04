import math
def calculate_powers(x, y, z):
    val1 = x**z
    val2 = x**(y**z)
    val3 = abs(x-y)
    val4 = math.sqrt(x**z)
    
    print(f'{val1:.2f}, {val2:.2f}, {val3:.2f}, {val4:.2f}')

def read_integers():
    user_input = input('Please enter a numerator and a denominator, separated by a comma\n')
    user_input = user_input.split(',')
    user_input = [int(ele) for ele in user_input]

    numerator = user_input[0]
    denominator = user_input[1]
    res = numerator // denominator
    for i in range(3):
        print(res)
        res = res // 2

def show_lab_vals(lab_vals: list):
    print(min(lab_vals))
    print(max(lab_vals))
    print(sum(lab_vals))

def remove_last(lab_vals: list):
    return lab_vals.pop()




print('Q1:')
calculate_powers(3,3,3)
print('---------------------------')
print('Q2:')
read_integers()
print('----------------------------')

lab_vals = [3,5,10,21,1]
print('Q3:')
show_lab_vals(lab_vals)
print('----------------')
print('Q4:')

print('before: ',lab_vals)
remove_last(lab_vals)
print('after: ',lab_vals)

