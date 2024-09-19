# Scorgs 91 - 100: Grade = "Outstanding”
# Scores 81 -90: Grade = "Exceeds Expectations”
# Scores 71-8o: Grade = "Acceptable”
# Scores 70 or lower: Grade = "Fail"
import json
from rich import print
def f091_graddingProgram():
    student_scores = {
            "Harry": 81,
            "Ron": 78,
            "Hermione": 99,
            "Draco": 74,
            "Neville": 62,
            }
    print(student_scores)
    student_grades = {}
    for student in student_scores:
        score = convertScore(student_scores[student])
        student_grades[student] = score
    print(f'student_grades: {json.dumps(student_grades,sort_keys=True, indent=4)}')

def convertScore(number):
    if(number >= 91 and number <= 100):
        return 'Outstanding'
    elif(number >= 81 and number <= 90):
        return 'Exceeds Expectations'
    elif(number >= 71 and number <= 80):
        return 'Acceptable'
    else:
        return 'Fail'

f091_graddingProgram()
