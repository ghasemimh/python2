# sef class student
class Student:
    def __init__(self , first_name , last_name , age , math_score , physics_score , python_score):
        #set variables
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.math_score = math_score
        self.physics_score = physics_score
        self.python_score = python_score
        
    def check_status(self):
        avg = (self.math_score + self.physics_score + self.python_score) / 3
        if avg >= 17:
            print("Accepted")
            
        else:
            print("Failed")
            
            
#input values
f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
age = input("Enter your age: ")
math_score = input("Enter your Math score: ")
physics_score = input("Enter your Physics score: ")
python_score = input("Enter your Python score: ")


#Check the values corrected


#Check age
while True:
    try:
        age = int(age)
        break
    
    except ValueError:
        age = input("Enter your age again: ")
 
#Check math_score   
while True:
    try:
        math_score = float(math_score)
        break
    
    except ValueError:
        math_score = input("Enter your Math score again: ")

#Check physics_score
while True:
    try:
        physics_score = float(physics_score)
        break
    
    except ValueError:
        physics_score = input("Enter your Physics score again: ")

#Check python_score
while True:
    try:
        python_score = float(python_score)
        break
    
    except ValueError:
        python_score = input("Enter your Python score again: ")

#call student class and set in 'person'
person = Student(f_name , l_name , age , math_score , physics_score ,  python_score)
person.check_status()