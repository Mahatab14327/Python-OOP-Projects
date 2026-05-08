class Student:
    def __init__(self, name, roll, subject_names, marks):
        self.name          = name
        self.roll          = roll
        self.subject_names = subject_names  
        self.marks         = marks          

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return round(self.total_marks() / len(self.marks), 2)

    def grade(self):
        avg = self.average_marks()
        if avg >= 80:
            return 'A+'
        elif avg >= 70:
            return 'A'
        elif avg >= 60:
            return 'A-'
        elif avg >= 50:
            return 'B'
        else:
            return 'F'

                        ###STUDENT INFO###

    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Roll Number:{self.roll}")
        for i in range(len(self.subject_names)):        
            print(f"Marks in {self.subject_names[i]}  : {self.marks[i]}")
        print(f"Total Marks:{self.total_marks()}")
        print(f"Average Marks:{self.average_marks()}")
        print(f"Grade:{self.grade()}")


                        ###MAIN PROGRAM###
print("===== Enter Student Information =====")
name = input("Enter Name:")
roll = input("Enter Roll:")
num  = int(input("How many subjects?:"))

subject_names = []
marks         = []

for i in range(num):                                    
    sub  = input(f"Enter Subject {i+1} Name:")
    mark = int(input(f"Enter {sub} Marks:"))
    subject_names.append(sub)
    marks.append(mark)

s1 = Student(name, roll, subject_names, marks)
s1.display_info()