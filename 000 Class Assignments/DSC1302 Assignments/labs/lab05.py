# 1.

# Complete the swap() method to exchange the values of the num attribute of two Number objects, num1 and num2. 

# Hint: Refer to the given Number class to see the definitions of num attribute and other instance methods available. 

# Ex: If num1 is 19 and num2 is 178, calling swap(num1, num2) will swap the values so that num1 becomes 178 and num2 becomes 19.




class Number:
    def __init__(self, n):
        self.num = n

    def get_num(self):
        return self.num

    def set_num(self, n):
        self.num = n

def swap(num1, num2):
    num1.num, num2.num = num2.num, num1.num
  # 
if __name__ == "__main__":
    int1 = int(input('input for num1:'))
    int2 = int(input('input for num2:'))

    num1 = Number(int1)
    num2 = Number(int2)

    swap(num1, num2)
    print(f'num1 = { num1.get_num() } and num2 = { num2.get_num() }')
    print('end of Q1----------------')





# Define a Course base class with the following attributes:

#     number - course number
#     title - course title

# Define a print_info() method in Course that displays the course number and title.

# Also define a derived class OfferedCourse with the additional attributes:

#     instructor_name - instructor name
#     location - class location
#     class_time - class time



class Course:
    def __init__(self, number, title):
        self.number = number
        self.title = title
    
    def print_info(self):
        print('Course Information:')
        print(f'Course number: {self.number}\nCourse Title: {self.title}')

class OfferedCourse(Course):
    def __init__(self, number, title, instructor_name, location, class_time):
        super().__init__(number, title) 
        self.instructor_name = instructor_name
        self.location = location
        self.class_time = class_time
    def print_info(self):
        print('Course Information:')

        print(f'Course number: {self.number}\nCourse Title: {self.title}\nInstructor: {self.instructor_name}\nLocation: {self.location}\nClass time: {self.class_time}')
        
    

if __name__ == "__main__":
    course_number = input('course number:')
    course_title = input('course title:')

    o_course_number =  input('offered course number2:')
    o_course_title =  input('offered course title:')
    instructor_name = input('instructor name:')
    location = input('location:')
    class_time = input('class time:')
    

    my_course = Course(course_number, course_title)
    my_course.print_info()
    
    my_offered_course = OfferedCourse(o_course_number, o_course_title, instructor_name, location, class_time)
    my_offered_course.print_info()

    print(f'   Instructor Name: { my_offered_course.instructor_name }')
    print(f'   Location: { my_offered_course.location }')
    print(f'   Class Time: { my_offered_course.class_time }')