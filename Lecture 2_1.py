##Queestion 1
##
##number = int(input("Enter number: "))
##
##if (number % 2 == 0):
##    print(f"{number} is even")
##else:
##    print(f"{number} is odd")    
##

##Question 2
##number1 = int(input("Enter first number: "))
##number2 = int(input("Enter second number: "))
##number3 = int(input("Enter third number: "))
##
##max = number1
##
##if (max < number2):
##    max = number2
##    
##if (max < number3):
##    max = number3
##
##print(max)

##Question3
##quiz = int(input("Enter quiz score: "))
##mid_term = int(input("Enter mid-term score: "))
##final_score = int(input("Enter final score: "))
##
##avg_score = float((quiz + mid_term + final_score) / 3)
##
##if (avg_score >= 90):
##    grade = 'A'
##elif (70 <= avg_score < 90):
##    grade = 'B'
##elif (50 <= avg_score < 70):
##    grade = 'C'
##elif (avg_score < 50):
##    grade = 'F'
##else:
##    print("Invalid")
##    
##print(avg_score)
####print(grade)
##
##Question 4
##import math
##
##a = int(input("Enter a: "))
##b = int(input("Enter b: "))
##c = int(input("Enter c: "))
##
##d = b ** 2 - 4 * a * c
##
##if (d > 0):
##    x1 = (-b - math.sqrt(d)) / (2 * a)
##    x2 = (-b + math.sqrt(d)) / (2 * a)
##    print(f"Two solutions: {x1} and {x2}")
##elif (d == 0):
##    x = -b / (2 * a)
##    print(f"One solution: {x}")
##else:
##    print("No real solutions")
##

##Question 5
##g = int(input("Enter money to return: "))
##
##if (g < 0):
##    print("Invalid input")
##elif(g == 0):
##    print("No money to return")
##else:
##    number_of_100 = g // 100
##    g %= 100
##
##    number_of_50 = g // 50
##    g %= 50
##
##    number_of_20 = g // 20
##    g %= 20
##
##    number_of_10 = g // 10
##    g %= 10
##
##    number_of_5 = g // 5
##    g %= 5
##
##    number_of_2 = g // 2
##    g %= 2
##
##    number_of_1 = g // 1
##
##    print(f"{number_of_100} 100 euro, {number_of_50} 50 euro, {number_of_20} 20 euro, {number_of_10} 10 euro, {number_of_5} 5 euro, {number_of_2} 2 euro, {number_of_1} 1 euro")
##

##Question 6
##height1 = int(input("Enter first student's height: "))
##height2 = int(input("Enter second student's height: "))
##height3 = int(input("Enter third student's height: "))
##height4 = int(input("Enter fourth student's height: "))
##height5 = int(input("Enter fifth student's height: "))
##
##avg_height = float((height1 + height2 + height3 + height4 + height5) / 5)
##
##taller_than_180 = 0
##smaller_than_164 = 0
##
##if (height1 > 180):
##    taller_than_180 += 1
##elif (height1 < 164):
##    smaller_than_164 += 1  
##
##if (height2 > 180):
##    taller_than_180 += 1
##elif (height2 < 164):
##    smaller_than_164 += 1
##    
##if (height3 > 180):
##    taller_than_180 += 1
##elif (height3 < 164):
##    smaller_than_164 += 1
##    
##if (height4 > 180):
##    taller_than_180 += 1
##elif (height4 < 164):
##    smaller_than_164 += 1
##    
##if (height5 > 180):
##    taller_than_180 += 1
##elif (height5 < 164):
##    smaller_than_164 += 1
##    
##print(f"Students taller than 180: {taller_than_180}, students smaller than 164: {smaller_than_164}, average height of students: {avg_height} ")

##Question 7
##number1 = int(input("Enter first number: "))
##number2 = int(input("Enter second number: "))
##
##if (number1 > 0 and number2 > 0):
##    print("Both numbers positive")
##elif (number1 < 0 and number2 < 0):
##    print("Both numbers negative")
##else:
##    print("One positive, one negative")

##Question 8
##year = int(input("Year you born: "))
##month = int(input("Month you born: "))
##
##if (month > 9):
##    age = 2026 - year - 1
##else:
##    age = 2026 - year
##    
##if month == 1:
##    month_name = "January"
##elif month == 2:
##    month_name = "February"
##elif month == 3:
##    month_name = "March"
##elif month == 4:
##    month_name = "April"
##elif month == 5:
##    month_name = "May"
##elif month == 6:
##    month_name = "June"
##elif month == 7:
##    month_name = "July"
##elif month == 8:
##    month_name = "August"
##elif month == 9:
##    month_name = "September"
##elif month == 10:
##    month_name = "October"
##elif month == 11:
##    month_name = "November"
##elif month == 12:
##    month_name = "December"
##else:
##    month_name = "Invalid Month"
##
##print(age, month_name)

##question 9
##a = int(input("Enter a: "))
##b = int(input("Enter b: "))
##
##if (a + b == 5):
##    print("Sum of numbers is 5")
##else:
##    print("Sum of numbers is not 5")

### task 10
##x = int(input("Enter number: "))
##
##if (x > 10):
##    print(x ** 2)
##else: 
##    print("x is less than 10")    



x = int(input("Enter x coordinate of dot: "))
y = int(input("Enter y coordinate of dot: "))

if (x > 0 and y > 0):
    print(f"({x}, {y}) First plane part")
elif( x < 0 and y > 0):
    print(f"({x}, {y}) Second plane part")
elif (x < 0 and y < 0):
    print(f"({x}, {y}) Third plane part")
elif (x > 0 and y < 0):
    print(f"({x}, {y}) Fourth plane part")
else:
    print("(0, 0) coordinate plane center")
