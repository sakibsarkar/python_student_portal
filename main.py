
class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

    @classmethod
    def find_student(cls, student_id):
        for student in cls.student_list:
            if student.get_student_id() == student_id:
                return student
        return None


class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    def get_student_id(self):
        return self.__student_id

    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
        else:
            print("Student is already enrolled.")

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
        else:
            print("Student is not enrolled.")

    def view_student_info(self):
        print("Student ID:", self.__student_id)
        print("Name:", self.__name)
        print("Department:", self.__department)
        print("Enrollment Status:", self.__is_enrolled)



Student(101, "Nora Fatehi", "CSE", False)
Student(102, "Tamanna vatia", "EEE", True)
Student(103, "Again Tamanna <3", "BBA", True)


while 1:
    print("\n1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for student in StudentDatabase.student_list:
            student.view_student_info()
            print(" ")

    elif choice == "2":
        try:
            student_id = int(input("Enter student ID: "))
            student = StudentDatabase.find_student(student_id)

            if student:
                student.enroll_student()
            else:
                print("Invalid student ID.")

        except ValueError:
            print("Invalid student ID.")

    elif choice == "3":
        try:
            student_id = int(input("Enter student ID: "))
            student = StudentDatabase.find_student(student_id)

            if student:
                student.drop_student()
            else:
                print("Invalid student ID.")

        except ValueError:
            print("Invalid student ID.")

    elif choice == "4":
        print("Closed...")
        break
