def averageHeight():
# You are going to write a program that calculates the average student
# height from a List of heights.
# . student_heights = (180, 124, 165, 173, 189, 169, 146)
# The average height can be calculated by adding all the heights
# together and dividing by the total number of heights.
# eg.
# 180 +124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in =tudent heights
# 1146 + 7 = 163.71428571428572
# Average height rounded to the nearest whole number = 164
# Important You should not use the «sum () o 1en() functions in your
# answer. You should try to replicate their functionality using what you
# have learnt abost for loops. e N >

# Example input
# 156 178 165 171 187
# In this case, student_heights would be a list that looks like: [156, 178,
# 165, 171, 187)
# Example Output
# e.g. When you hit run, this is what should happen:
# 2e
# ryien
# 16, 1 9 2019, 00106143)
# 61 on hima
# I List o tagent bdahca 156 170 165 171 147
# i
# Hint
# 1. Remember to use the =cusci() function to round the average
# height before you print i


# 8 Don't change the code below &
    student_heights = input("Input a list of student heights ").split(' ')
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])
    print(student_heights)
    sum_heights = sum(student_heights)
    total_length = len(student_heights)
    average = round(sum_heights / total_length)
    print(average)

    sum_heights = 0
    for height in student_heights:
        sum_heights += height
    total_length = 0
    for height in student_heights:
        total_length += 1
    average = round(sum_heights / total_length)
    print(average)

# 8 Don't change the code above &
#rite your code below this row %
averageHeight()
