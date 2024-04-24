#!/bin/python3

import os

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        grade = grades[i]
        if grade < 38:
            continue
        str_grade = str(grade)
        if int(str_grade[1]) > 5:
            diff = 10 - int(str_grade[1])
        else:
            diff = 5 - int(str_grade[1])

        if diff < 3:
            grades[i] = grade + diff

    return grades


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
