class student:

    def __init__(self,name,roll_number,cgpa):

        self.name=name

        self.roll_number = roll_number

        self.cgpa = cgpa

def sort_students(student_list):

       sorted_students = sorted(student_list,key= lambda student: student.cgpa,reverse=True)



       return sorted_students



students=[

    student("priya","a198",8.9),

    student("venki","a173",7.5),

    student("Praveen","a193",7.7),

    student("jeeva","a178",7.4),

    ]

sorted_students=sort_students(students)



for students in sorted_students:

    print("Name: {},Roll Number: {},CGPA: {}".format(students.name,students.roll_number,
students.cgpa))
