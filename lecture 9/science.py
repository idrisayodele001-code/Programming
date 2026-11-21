##task 1
##from datetime import date
##
##file = open("science.txt", "r")
##lines = file.readlines()
##file.close()
##
##today = date.today()
##
##output = open("IT_scientists.txt", "w")
##
##for line in lines:
##    surname, name, science, code = line.split()
##
##    gender = code[0]
##    year = int(code[1:3])
##    month = int(code[3:5])
##    day = int(code[5:7])
##
##    if gender == "4":
##        birth_year = 1900 + year
##
##    elif gender == "6":
##        birth_year = 2000 + year
##
##    else:
##        continue
##
##    age = today.year - birth_year
##
##    if (today.month, today.day) < (month, day):
##        age -= 1
##
##    if science == "informatics" and 35 < age < 55:
##        output.write(surname + " " + name[0] + ". " + str(age) + "\n")
##
##output.close()

##task 2
##def sum_negative(numbers):
##    total = 0
##
##    for number in numbers:
##        if number < 0:
##            total = total + number
##
##    return total
##
##
##my_list = [5, -2, 8, -4, 3, -6]
##
##result = sum_negative(my_list)
##
##print(result)

##Task 3
##m = int(input("Enter number of students: "))
##n = int(input("Enter number of marks: "))
##
##Students = []
##
##for i in range(m):
##    row = []
##    for j in range(n):
##        mark = float(input("Enter mark: "))
##        row.append(mark)
##    Students.append(row)
##
##AVG = []
##
##for i in range(m):
##    total = 0
##
##    for j in range(n):
##        total = total + Students[i][j]
##
##    average = total / n
##    AVG.append(average)
##
##print("Student averages:")
##
##for i in range(m):
##    print("Student", i + 1, ":", AVG[i])
##
##best = AVG[0]
##best_student = 0
##
##for i in range(m):
##    if AVG[i] > best:
##        best = AVG[i]
##        best_student = i
##
##print("Best student:", best_student + 1)
##print("Highest average:", best)
