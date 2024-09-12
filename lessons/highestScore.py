def highestScore():
    score = 0;
    student_score = [78,65,89,86,55,64,89]
    for student in student_score:
        if student > score:
            score = student

    print(f"The highest score in the class is: {score}")

highestScore()
