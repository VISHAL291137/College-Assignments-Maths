def create_student_record(name, roll_no, admission_no, marks):
    student_record = {
        "Name": name,
        "Roll Number": roll_no,
        "Admission Number": admission_no,
        "Marks": marks
    }
    return student_record

def main():
    # Taking user input for student information
    name = input("Enter student's name: ")
    roll_no = input("Enter student's roll number: ")
    admission_no = input("Enter student's admission number: ")
    marks = float(input("Enter student's marks: "))

    # Creating a dictionary for the student using the create_student_record function
    student_dict = create_student_record(name, roll_no, admission_no, marks)

    # Printing the student information
    print("\nStudent Information:")
    for key, value in student_dict.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
