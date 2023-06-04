def draw_triangle(size: int):
    def _recursive_helper(n: int):

        if n <= 0:
            return

        spacing = ' '
        star = '*'
        statement = spacing * ((size - n) // 2)
        print(statement + star*n + statement)
        _recursive_helper(n-2)

    _recursive_helper(size)
        
    
def correct_order(file_name: str):
    beginning = input('Term for the beginning part of the search: \n')
    last = input('Term for the last part of the search: \n')
    boundary = [beginning, last]

    with open(file_name, 'r') as reader:
        reader.seek(0)
        for word in reader.readlines():
            if word < boundary[0] or word > boundary[1]:
                print(word.strip(), 'not in range')
            else:
                print(word.strip(), 'in range')
             
            
    


if __name__ == '__main__':
    base_length = int(input())
    draw_triangle(base_length)
    print('end of Q1: ---------------------')

    correct_order('input_text.txt')
    

