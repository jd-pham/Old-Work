

def print_all_permutations(permList, nameList):
    # TODO: Implement method to create and output all permutations of the list of names.
    def recursive_helper(message, list1):
        if not list1:
            print(message[:-1])
            return
        recursive_helper(message + list1[-1] + ', ', list1[:-1])
    
    for i, name in enumerate(nameList):
        recursive_helper(name + ', ', nameList[:i] + nameList[i + 1:])





    # if __name__ == "__main__": 
        # nameList = input().split(' ')
permList = []
nameList = ['Josh', 'Tom', 'Jake']

print_all_permutations(permList, nameList)


print('end of Q1 ----------------------------')

    # Define custom exception
class StudentInfoError(Exception):
    def __init__(self, message):
        self.message = message  # Initialize the exception message


def find_ID(name, info):
    if name in info:
        return info[name]
    raise StudentInfoError('No student exists with such name')
    
def find_name(ID, info):
    for student_name, student_id in info.items():
        if student_id == ID:
            return student_name
    raise StudentInfoError('No student with such ID')


if __name__ == '__main__':
    # Dictionary of student names and IDs
    student_info = {
        'Reagan' : 'rebradshaw835',
        'Ryley' : 'rbarber894',
        'Peyton' : 'pstott885',
        'Tyrese' : 'tmayo945',
        'Caius' : 'ccharlton329'
    }
    
    userChoice = input('pick a choice to search')    # Read search option from user. 0: find_ID(), 1: find_name()
    
    # FIXME: find_ID() and find_name() may throw an Exception.
    #        Insert a try/except statement to catch the exception and output any exception message.

    try:
        if userChoice == "0":
            name = input()
            result = find_ID(name, student_info)
        else:
            ID = input()
            result = find_name(ID, student_info)
        print(result)
    except StudentInfoError as e:
        print(e.message)

    

print('end of Q2 ----------------------------')

def print_num_pattern(num1, num2):
    def _helper(n1, reversed = False):
        # if n1 == num1 and reversed:
        #     return
        
        print(n1, end=' ')
        if not reversed:
            if n1 != -num1:
                return _helper(n1 - num2)
            else:
                return _helper(n1 + num2, reversed=True)
        else:
            if n1 != num1:
                return _helper(n1 + num2, reversed)
            else:
                return
    _helper(num1)



    # TODO: Write recursive print_num_pattern() function

if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print_num_pattern(num1, num2)

