##Task 1
##v = int(input("Average books per month: "))
##n = int(input("Average visits per year: "))
##
##k = (n / 12) * v * 12
##
##print(f"Average books per year one visitor reads {round(k)} books")

# Task 2
# x1 = int(input("Enter x1 coordinate: "))
# y1 = int(input("Enter y1 coordinate: "))
# x2 = int(input("Enter x2 coordinate: "))
# y2 = int(input("Enter y2 coordinate: "))

# width = abs(y2 - y1)
# length = abs(x2 - x1)

# s =  width * length
# p = 2 * (width + length)

# print(f"Area: {s}, perimeter: {p}")

# Task 3
# from math import pi

# r_small = int(input("Enter radius of small circle: "))
# r_middle = r_small * 2
# r_big = r_middle * 2

# area_small = round(pi * r_small ** 2, 2)
# area_middle =  round(pi * r_middle ** 2, 2)
# area_big = round(pi * r_big ** 2, 2)

# print(f"r = {r_small}, the areas of circles are {area_small}, {area_middle}, {area_big}")

# Task 4
# n = int(input("Enter salary per month: "))

# print(f"Monthly income: {n}")

# taxes = float(n / 20)

# n -= taxes

# food = float(n / 2)
# clothes = float(n * 3 / 10)

# n -= food + clothes

# entertaintment = n

# print(f"Taxes: {taxes}, food: {food}, clothes: {clothes}, entertaintment: {entertaintment}")

# Task 5
# n = int(input("Enter 4-digit number: "))

# sign = -1 if n < 0 else 1

# reversed_n = int(str(abs(n))[::-1])

# print(sign * reversed_n)
   
# Task 6
# n1 = int(input("Enter 1 if student complete homework, 0 if not: "))
# n2 = int(input("Enter 1 if student has neat notes, 0 if not: "))
# n3 = int(input("Enter 1 if student not misses classes, 0 if not: "))

# if (n1 == 0 or n2 == 0 or n3 == 0):
#     print("Student will not get 10")
# else:
#     print("Student will get 10")  

# Task 7
# k = int(input("Jolanta's budget for trip: "))

# if (k < 1000):
#     print("Jolanta best for trip group 4")
# elif (1000 <= k <= 2999):
#     print("Jolanta best for trip group 3")
# elif (3000 <= k <= 3999):
#     print("Jolanta best for trip group 2")
# else:
#     print("Jolanta best for trip group 1")    

# Task 8
# ticket = int(input("Enter ticket number: "))

# sum_of_digits = 0

# for digit in str(ticket):
#     sum_of_digits += int(digit)

# print(sum_of_digits)

# if sum_of_digits % 4 == 0:
#     print("You win the lottery")
# else:
#     print("You lose the lottery")

# Task 9
# N = int(input("Enter 4-digit number: "))

# first_two = N // 100
# last_two = N % 100

# if (first_two + last_two) ** 2 == N:
#     print("This is interesting situation")
# else:
#     print("This is not interesting situation")
