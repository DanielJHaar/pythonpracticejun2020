# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:17:36 2020

@author: danie
"""


from collections import namedtuple

n = int(input())
fields = input().split()

total_marks = 0
for _ in range(n):
    students = namedtuple('student', fields)
    MARKS, CLASS, NAME, ID = input().split()
    student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(student.MARKS)
print(round((total_marks/n),2))