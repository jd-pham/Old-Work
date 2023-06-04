import numpy as np


# Q1
print('START Q1 ----------------------------------------\n')

array = [5, 9, 2, 1, 8, 4, 6, 12, 3, 10, 7, 11]

array_3d = np.array(array)
array_3d = array_3d.reshape(4,3)
print(array_3d)
print('\nEND OF Q1 ---------------------------------------------\n')



# Q2
multiplied_array = np.dot(array_3d, array_3d.T)
print(multiplied_array)
print('\nEND OF Q2 ---------------------------------------------\n')


# Q3
array = np.array([3,5,23,54,32,45,123,12])
print('before split:', array,)
split_array = np.split(array, 2)

print('after split:')
for ele in split_array:
    print(ele)
