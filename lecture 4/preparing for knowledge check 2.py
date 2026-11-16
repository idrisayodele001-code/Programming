##Task 1
##print("-----------------------------")
##print("I     x      I     y     I")
##print("-----------------------------")
##
##for x in range(-10, 11):
##     y = 7 * (x ** 2) + 5 * x - 3
##     print("I%7d     I   %7.2f    I" %(x, y))
##print("------------------------------")
##

# Task 2
# n = int(input("Number of laps: "))
# m = int(input("Length of one lap: "))
# t = 0

# for i in range(n):
#     tt = int(input(f"Enter time spent for {i + 1} lap: "))
#     t += tt

# average_speed = float(m * n / t)

# print(f"The athlete's average speed v = {average_speed:.1f} m/s, the distance was covered in {t} seconds")

# Task 3
# n = int(input("Number of stages: "))
# k = int(input("Number of targets: "))
# b = int(input("Enter penalty minutes for each shot: "))

# t = 0

# for i in range(n):
#     tt = int(input("Minutes to complete stage: "))
#     kk = int(input("Number of targets hitted: "))
#     added_penalty = (k - kk) * b
#     t += tt + added_penalty
    
# print(f"The athlete completed track in {t} minutes")

# Task 4
# b = int(input("Strawberries ripened in first day: "))
# d = int(input("Number of more strawberries each subsequest day: "))
# n = int(input("Enter day count to calculate strawberry count: "))

# strawberry_count = 0

# for day in range(n):
#     strawberry_count += b + d * day

# print(f"{strawberry_count} strawberries rippened in {n} days")

# Task 5
# p1 = int(input("Enter initial price: "))
# n = int(input("Number of participants: "))

# p2 = p1

# for i in range(n):
#     d1 = int(input("Enter proposed increase in price: "))
#     p2 += d1

# print(f"The final price of the item will be {p2} euros")

# Task 6
# n = int(input("Enter member count: "))

# sum = 0
# first = 2
# second = 3

# for i in range(n):
#     sum += first * second
#     first += 1
#     second += 2
    
# print(sum)

# Task 7
# a = int(input("Current salary: "))
# x = int(input("Monthly increase in salary: "))
# n = int(input("Enter number of months: "))
# b = int(input("Enter minimum salary: "))

# print(f"Salary after a year: {a + 12 * x}")
# print(f"Salary after {n} months: {a + x * n}")

# month_count = 0
# doubled_salary = a * 2
# salary = a

# while salary <= doubled_salary:
#     month_count += 1
#     salary += x
    
# print(f"After {month_count} months, salary surpass its double {doubled_salary} with latest of {salary}")

# months = 0

# while a < b:
#     months += 1
#     a += x

# print(f"After {months} months, salary {a} is at least {b}")

# Task 8
# initial_deposit = int(input("Enter initial deposit: "))
# annual_interest = int(input("Enter annual interest: "))
# m = int(input("Enter years to calculate deposit value: "))

# total_money = initial_deposit

# for i in range(m):
#     added_money = total_money * annual_interest / 100
#     total_money += added_money

# print(total_money)

# Task 9
# whole_grade = 0
# number_of_classes = 0

# while True:
#     grade = int(input("Enter grade: "))
    
#     if grade == 0:
#         break
    
#     whole_grade += grade
#     number_of_classes += 1
    
# average_grade = whole_grade / number_of_classes
# print(average_grade)

# Task 10
# n = int(input("Number of circles: "))
# circles_radius = []

# for i in range(n):
#     circles_radius.append(int(input("Enter radius: ")))

# max_radius = max(circles_radius)

# print(f"Largest circle radius is {max_radius}")
# print(f"Amount of circles with radius {max_radius} is {circles_radius.count(max_radius)}")

# Task 11
# grades = []
# grade = int(input("Enter grade: "))

# while grade != 0:
#     grades.append(grade)
#     grade = int(input("Enter grade: "))
    
# print(f"Average is {sum(grades) / len(grades)}")

# Task 12
# n = int(input("Enter number of products: "))
# A = []
# B = []

# for i in range(n):
#     A.append(int(input("Number of units of product: ")))

# for i in range(n):
#     B.append(int(input("Number of product units to added: ")))

# print(A)
# print(B)

# for product in range(n):
#     A[product] = A[product] + B[product]

# print(A)

# Task 13
# n = int(input("Number of children: "))
# A = []

# for i in range(n):
#     A.append(int(input("Enter number of non-attendance days: ")))

# ascending_A = sorted(A)
# descending_A = sorted(A, reverse = True)
# print(A)
# print(ascending_A)
# print(descending_A)

# Task 14
# n = int(input("Number of people: "))
# weight_list = []
# category_1 = []
# category_2 = []
# category_3 = []

# for people in range(n):
#     weight = int(input("Enter person's weight: "))
#     weight_list.append(weight)
    
#     if weight > 80:
#         category_3.append(weight)
#     elif weight >= 60:
#         category_2.append(weight)
#     else:
#         category_1.append(weight)
    
# print(weight_list)
# print(f"{len(category_1)} people in category 1")
# print(f"{len(category_2)} people in category 2")
# print(f"{len(category_3)} people in category 3")

# Task 15
# n = int(input("Number of sections in library: "))
# A = []

# for i in range(n):
#     A.append(int(input("Number of cards: ")))
    
# print(A)

# for i in range(1, n, 2):
#     A[i] = A[i] + i + 1

# print(A)
