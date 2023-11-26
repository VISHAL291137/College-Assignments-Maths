class Student:
    def __init__(self, name, roll_no, admission_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.admission_no = admission_no
        self.marks = marks

    def display_info(self):
        print("\nStudent Information:")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Admission Number:", self.admission_no)
        print("Marks:", self.marks)

def main():
    # Taking user input for student information
    name = input("Enter student's name: ")
    roll_no = input("Enter student's roll number: ")
    admission_no = input("Enter student's admission number: ")
    marks = float(input("Enter student's marks: "))

    # Creating an instance of the Student class
    student1 = Student(name, roll_no, admission_no, marks)

    # Displaying the student information using the display_info method
    student1.display_info()

if __name__ == "__main__":
    main()
