class Student:
    
    def __init__(self,name,roll_no,marks):
                
            self.name = name
            self.roll_no = roll_no
            self.marks = marks
                
    def calculate_average(self):
        total = sum(self.marks.values())
        return total / len(self.marks)
    
    def calculate_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return 'A+'
        elif average >= 80:
            return 'A'
        elif average >= 70:
            return 'B'
        elif average >= 60:
            return 'C'
        elif average >= 50:
            return 'D'
        else:
            return 'F'
        
    def report_card(self):
        print(f"\n--- Report Card ---")
        print(f"Name     : {self.name}")
        print(f"Roll No  : {self.roll_no}")
        print("Marks    :")
        for subject, mark in self.marks.items():
            print(f" {subject}: {mark}")
        print(f"Average  : {self.calculate_average():.2f}")
        print(f"Grade    : {self.calculate_grade()}")
        
def main():
    name = input("Enter your name: ")
    roll_no = int(input("Enter your roll number: "))
    
    subjects = ["Science","Maths","Chemistry","Gujarati"]
    marks = {}
    
    for subject in subjects:
        while True:
            try:
                score = int(input(f"Entre your marks for {subject} "))
                if 0 <= score <= 100:
                   break
                else:
                    print("Marks must be between 0 to 100, usaki yaado mai mat kho jao sahi marks dalo firse :)")
            except ValueError:
                print("plz Enter valid marks")
        marks[subject] = score
    
    student = Student(name,roll_no,marks)
    student.report_card()
    
    

    