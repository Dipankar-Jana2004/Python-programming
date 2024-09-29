class Student:
    def _init_(self,Student_Id,Name,email,phone_no):
        self.Student_Id=Student_Id
        self.Name=Name
        self.email=email
        self.phone_no=phone_no

class System(Student):
    def _init_(self):
        self.students={}
        self.deleted_students={}
    def show_student_list(self):
        if not self.students:
            print("No student to show in list")
        else:
            for Student_Id, students in self.students.items():
                print(f"Student_Id:{Student_Id} Name:{students.Name} Email:{students.email}")

    def show_student_detils(self,Student_Id):
        Student=self.students.get(Student_Id)
        if Student:
            print(f"Student_Id:{Student_Id} Name:{Student.Name} Email:{Student.email} Phone_no:{Student.phone_no}")
        else:
            print("Student not founded.")

    def add_new_student(self,Student_Id,Name,email,phone_no):
        if Student_Id in self.students:
            print("Student Id have already exists.")
        else:
            new_student=Student(Student_Id,Name,email,phone_no)
            self.students[Student_Id]=new_student
            print("New student added successfully in system.")
    
    def update_student_details(self,Student_id,Name=None,email=None,phone_no=None):
        Student=self.students.get(Student_id)
        if Student:
            if Name:
                Student.Name=Name
            if email:
                Student.email=email
            if phone_no:
                Student.phone_no=phone_no
                print("Student details updated in system")
        else:
            print("Student not found.")
    def remove_student(self,Student_Id):
        if Student_Id in self.students:
            print("Student found.")
            remove_student=self.students.pop(Student_Id)
            self.deleted_students[Student_Id]=remove_student
            print(f"Student {Student_Id} removed.")
        else:
            print("Student not found.")

    def show_deleted_students(self):
        if not self.deleted_students:
            print("Deleted students not to show in system")
        else:
            for Student_id, Student in self.deleted_students.items():
                print(f"Deleted_Student_Id:{Student_id} Name:{Student.Name}")
    def output(self):
        while True:
            print("\n Options")
            print("1. Show Student list")
            print("2. Show Student Details")
            print("3. Add new Student")
            print("4. Update a Student Details")
            print("5. Remove a Student")
            print("6. Show Deleted Student")
            print("7. Quit")
            choice=input("Enter your choice: ")
            if choice=="1":
                self.show_student_list()
            if choice=="2":
                Student_Id=input("Enter your Student_Id:")
                self.show_student_detils(Student_Id)
            elif choice=="3":
                Student_Id=input("Enter the Student Id: ")
                Name=input("Enter the student name: ")
                email=input("Enter student email: ")
                phone_no=input("Enter student phone_no: ")
                self.add_new_student(Student_Id,Name,email,phone_no)
            elif choice=="4":
                Student_Id=input("Enter the student_id: ")
                Name=input("Enter the student name: ")
                email=input("Enter student email: ")
                phone_no=input("Enter student phone_no: ")
                self.update_student_details(Student_Id,Name,email,phone_no)
            elif choice=="5":
                Student_Id=input("Enter the Student_id: ")
                self.remove_student(Student_Id)
            elif choice=="6":
                self.show_deleted_students()
            elif choice=="7":
                print("Exit the program..")
                break
            else:
                print("Invallid choice..")
Control_system=System()
Control_system.output()