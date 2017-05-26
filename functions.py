students=[]

def get_students():
    student_name=[]
    for student in students:
        student_name=student["student_name"].title()
        student_id = student["student_id"].title()
        return student_name , student_id


def print_students():
    print_s = get_students()
    print(print_s)


def add_students(name, id):
    student = {"student_name": name, "student_id": id}
    students.append(student)

student_list = get_students()

student_name = input("Enter a name : ")
student_id = input("Enter an id : ")

add_students(student_name, student_id)
print_students()
