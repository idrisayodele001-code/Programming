##Task 1                        
##n = int(input("How many integers: "))
##
##numbers = []
##
##for i in range(n):
##     numbers.append(int(input("Enter number: ")))
##
##count = sum(numbers) ** 2
##average = float(sum(numbers) / n)
##
##sum_of_positives = 0
##multiplication_of_negatives = 1
##
##for number in numbers:
##     if number > 0:
##         sum_of_positives += number
##     elif number < 0:
##         multiplication_of_negatives *= number
##        
##print(count, average, sum_of_positives, multiplication_of_negatives)

# Task 2
# m = int(input("Enter minimum year: "))
# n = int(input("Enter maximum year: "))

# leap_year_count = 0

# for year in range(m, n + 1):
#     if year % 4 == 0:
#         leap_year_count += 1

# print(leap_year_count)

# Task 3
# number_of_rows = int(input("Enter number of rows: "))
# chairs_in_one_row = int(input("Enter number of chairs in first row: "))

# number_of_chairs_needed = 0

# for row in range(number_of_rows):
#     number_of_chairs_needed += chairs_in_one_row
#     chairs_in_one_row += 2

# print(number_of_chairs_needed)    

# Task 4
# n = int(input("Enter child's age: "))

# all_money = 5

# for year in range(n):
#     all_money += year + 1
    
# print(all_money)

# Task 5
# m = int(input("Enter m: "))
# n = int(input("Enter n (n > m): "))

# for number in range(m, n + 1):
#     print(f"Numbers {number}")
    
#     sum_of_digits = 0
#     for digit in str(number):
#         sum_of_digits += int(digit)
#     print(f"sum of digits is {sum_of_digits}")
    
#     if (sum_of_digits % 2 == 0):
#         print("It is even")
#     else:
#         print("It is odd")

# Task 6
# n = int(input("Enter minimum of range: "))
# m = int(input("Enter maximum of range: "))

# interesting_numbers = []

# for number in range(n, m + 1):
#     sum_of_cubes = 0
    
#     for digit in str(number):
#         sum_of_cubes += int(digit) ** 3
    
#     if sum_of_cubes == number:
#         interesting_numbers.append(number)
    
#     sum_of_cubes = 0

# print(interesting_numbers)

# Task 7
# savings = [
#     [6, 1.7, 4.3, 5],                 
#     [7, 5.5, 6.2, 6.1, 2.2, 6],       
#     [8.56, 3.33, 7],                  
#     [6, 8, 3.3, 6, 1.4],   
#     [7, 9.2, 2.5, 6, 5],           
#     [7, 3.3, 5, 2, 5, 7]              
# ]
    
# total = sum(sum(month) for month in savings)

# print(total)
