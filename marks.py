class Student:
    def __init__(self, name):
        self.name = name
        self.marks = {}

    def a_sub(self, subject, mark):
        self.marks[subject] = mark

    def totalMarks(self):
        return sum(self.marks.values())

    def percent(self):
        ttl_obtained = self.totalMarks()
        max_marks = len(self.marks) * 100  
        if max_marks > 0:
            return (ttl_obtained / max_marks) * 100
        return 0

student = Student("John Doe")
student.a_sub("UkrMova", 100)
student.a_sub("Math", 80)
student.a_sub("Chemistry", 78)

print(f"Total Marks: {student.totalMarks()}")
print(f"Percentage: {student.percent()}%")

student.a_sub("Math", 95)

print(f"Total Marks after updating 'Math': {student.totalMarks()}")
print(f"Percentage after updating 'Math': {student.percent()}%")



