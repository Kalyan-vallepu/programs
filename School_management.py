class Student:
    """
    Represents a student with basic information.
    """
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    def __str__(self):
        return f"Student: {self.name}, Roll No: {self.roll_no}, Grade: {self.grade}"

class Teacher:
    """
    Represents a teacher with basic information.
    """
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"Teacher: {self.name}, Subject: {self.subject}"

class School:
    """
    Represents a school with basic functionalities.
    """
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def get_students(self):
        return self.students

    def get_teachers(self):
        return self.teachers

    def display_students(self):
        print(f"Students of {self.name}:")
        for student in self.students:
            print(student)

    def display_teachers(self):
        print(f"Teachers of {self.name}:")
        for teacher in self.teachers:
            print(teacher)

# Example Usage
if __name__ == "__main__":
    school = School("ABC School")

    # Create students
    student1 = Student("Alice", 1, "A")
    student2 = Student("Bob", 2, "B")
    school.add_student(student1)
    school.add_student(student2)

    # Create teachers
    teacher1 = Teacher("Mr. Smith", "Math")
    teacher2 = Teacher("Ms. Jones", "Science")
    school.add_teacher(teacher1)
    school.add_teacher(teacher2)

    # Display students and teachers
    school.display_students()
    school.display_teachers()