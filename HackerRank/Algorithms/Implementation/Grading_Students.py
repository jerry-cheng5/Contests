'''
HackerRank
Grading Students
https://www.hackerrank.com/challenges/grading/problem
Jerry Cheng
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    new_grades = []
    for grade in grades:
        if grade >= 38:
            if (grade+2) % 5 == 0:
                new_grades.append(grade + 2)
            elif(grade+1) % 5 == 0:
                new_grades.append(grade + 1)
            else:
                new_grades.append(grade)
        else:
            new_grades.append(grade)
    return new_grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
