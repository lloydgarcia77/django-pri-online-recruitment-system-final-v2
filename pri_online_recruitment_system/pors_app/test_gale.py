# https://towardsdatascience.com/gale-shapley-algorithm-simply-explained-caa344e643c2
# lloyd = {
#     "name": "Lloyd",
#     "homework": [90.0, 97.0, 75.0, 92.0],
#     "quizzes": [88.0, 40.0, 94.0],
#     "tests": [75.0, 90.0]
# }
# alice = {
#     "name": "Alice",
#     "homework": [100.0, 92.0, 98.0, 100.0],
#     "quizzes": [82.0, 83.0, 91.0],
#     "tests": [89.0, 97.0]
# }
# tyler = {
#     "name": "Tyler",
#     "homework": [0.0, 87.0, 75.0, 22.0],
#     "quizzes": [0.0, 75.0, 78.0],
#     "tests": [100.0, 100.0]
# }

# students = [lloyd, alice, tyler]

# count = 0
# for student in students:
#     print students[count]['name']
#     print students[count]['homework']
#     print students[count]['quizzes']
#     print students[count]['tests']
#     count += 1
# for pupil in students:
#     print pupil["name"]
#     ...etc

import xlrd

# Give the location of the file 
loc = ("C:\\Users\\lloyd.garcia\\Documents\\MyFirstDjangoProj\\PRI_Online_Recruitment_System\\Attendance Sept 21 - Oct 5, 2019.xls")

# To open Workbook 
print(loc)
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(1)

# For row 0 and column 0 
print(sheet.cell_value(1, 1) )

# Extracting number of rows 
print(sheet.nrows) 
# Extracting number of columns 
print(sheet.ncols) 

for i in range(sheet.ncols): 
    print(sheet.cell_value(0, i)) 

for i in range(sheet.nrows): 
    print(sheet.cell_value(i, 0)) 

# Program to extract a particular row value 
print(sheet.row_values(1)) 