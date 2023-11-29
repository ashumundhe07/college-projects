import os
import json

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.data_file = "students.json"
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                self.students = json.load(file)

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump(self.students, file, indent=2)

    def add_student(self, name, enrollment, grades=None, attendance=None):
        new_student = {
            "name": name,
            "enrollment": enrollment,
            "grades": grades if grades else [],
            "attendance": attendance if attendance else {}
        }
        self.students.append(new_student)
        self.save_data()

    def display_students(self):
        for student in self.students:
            print(f"Name: {student['name']}, Enrollment: {student['enrollment']}")
            print(f"Grades: {student['grades']}")
            print(f"Attendance: {student['attendance']}")
            print("-" * 30)

    def update_grades(self, enrollment, new_grades):
        for student in self.students:
            if student['enrollment'] == enrollment:
                student['grades'] = new_grades
                self.save_data()
                print(f"Grades updated for {student['name']} ({enrollment})")

    def mark_attendance(self, enrollment, date, status):
        for student in self.students:
            if student['enrollment'] == enrollment:
                if enrollment not in student['attendance']:
                    student['attendance'][enrollment] = {}
                student['attendance'][enrollment][date] = status
                self.save_data()
                print(f"Attendance marked for {student['name']} ({enrollment}) on {date}")

# Example Usage
sms = StudentManagementSystem()

# Add students
sms.add_student("John Doe", "E001", grades=[90, 85, 88], attendance={"2022-01-01": "Present", "2022-01-03": "Absent"})
sms.add_student("Jane Smith", "E002", grades=[78, 92, 80], attendance={"2022-01-01": "Absent", "2022-01-03": "Present"})

# Display students
sms.display_students()

# Update grades
sms.update_grades("E001", [92, 88, 94])

# Mark attendance
sms.mark_attendance("E002", "2022-01-10", "Present")

# Display updated students
sms.display_students()
