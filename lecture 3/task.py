##Task 1
##a = int(input("Enter number: "))
##
##c = 0
##
##while a != 0:
##    c += 1
##    a //= 10
##    
##print(f"The amount of digits: {c}")

##task 2
##a = int(input("Enter number: "))
##
##while a >= 10:
##    a //= 10
##    
##print(f"First digit of number is: {a}")

##Task 3
##i = 1
##sum = 0
##
##while (1 / i ** 2) > 0.001:
##    member = 1 / i ** 2
##    sum += member
##    print(i)
##    i += 1
##
##print(pow(3.14159, 2) / 6 - sum)

##m = int(input("Enter number: "))
##print(f"Multiplication table for {m}")
##
##i = 1
##
##while i <= 10:
##    print(f"{m} * {i} = {m * i}")
##    i += 1
##

##Task 4
##m = int(input("Enter number: "))
##print(f"Multiplication table for {m}")
##
##i = 1
##
##while i <= 10:
##    print(f"{m} * {i} = {m * i}")
##    i += 1

##Task 5
##a = int(input("Enter a: "))
##b = int(input("Enter b: "))
##
##tshirt = 0
##i = a
##
##while (i <= b):
##    if (i % 6 == 0):
##        tshirt += 1
##    i += 1

##task 6
##all_nuts = int(input("How many nuts squirrel accimulated: "))
##little_squirrels = int(input("How many little squirrel: "))
##
##nuts_per_day = (little_squirrels + 1) * 3
##
##days_nuts_last = 0
##
##i = all_nuts
##
##while (i >= nuts_per_day):
##    days_nuts_last += 1
##    i -= nuts_per_day
##
##print(f"Result: there are enough nuts for {days_nuts_last} days.")
##
##if (days_nuts_last > 92):
##    print("Nuts will be enough for the whole winter.")
##else: 
##    print("Nuts will be not enough for the whole winter.")
##
##print(f"{tshirt} t-shirts needed")
