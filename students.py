#!/usr/bin/env python3
num = int(input('Enter the number of students:'))
data = {}
subjects = ('Physics','Maths','History')
for i in range(0,num):
    name = input('Enter the name of the students:').format(i+1)
    marks = []
    for x in subjects:
        marks.append(int(input('Enter marks of {}:').format(x)))
    data[name] = marks
for x,y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x,total))
    if total <120:
        print(x,'failed:(')
    else:
        print(x,'passed:)')
