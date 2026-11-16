##Task 1
##n = int(input("Enter number of elements in array: "))
##m = int(input("Enter element to count: "))
##
##A = []
##
##for i in range(n):
##     A[i:i+1] = [int(input("Enter number: "))]
##    
##print(A)
##print(f"Count of {m} is {A.count(m)}")

# Task 2
# n = int(input("Number of students: "))

# H = []

# for i in range(n):
#     H[i:i+1] = [float(input("Enter height: "))]

# average = float(sum(H) / n)

# count = 0

# for height in H:
#     if height > average:
#         count += 1

# print(average)
# print(f"{count} students taller than average")

# Task 3
# m = int(input("Number of elements in A: "))
# n = int(input("Number of elements in B: "))

# A = []
# B = []

# for a in range(m):
#     A[a:a+1] = [int(input("Enter element for A: "))]
    
# for b in range(n):
#     B[b:b+1] = [int(input("Enter element for B: "))]

# print(A)
# print(B)
    
# for i in range(m):
#     if A[i] > 12 : A[i] = 0

# for i in range(n):
#     if B[i] < 0 : B[i] = sum(A)


# print(A)
# print(B)

# Task 4
# n = int(input("Number of people: "))

# A = []
# low_salary = 0
# middle_salary = 0
# high_salary = 0

# for i in range(n):
#     A[i:i+1] = [int(input("Enter salary: "))]
    
# if A[i] > 800:
#     high_salary += 1
# elif A[i] > 600:
#     middle_salary += 1
# elif A[i] >= 300:
#     low_salary += 1
    
# print(A)


# print(f"The number of people, receiving: 300 to 600 is {low_salary}, 600 to 800 is {middle_salary}, more than 800 is {high_salary}")

# Task 5
# n = int(input("Number of elements in A: "))
# m = int(input("Number of elements in B: "))

# A = []
# B = []

# for a in range(n):
#     A[a:a+1] = [int(input("Enter element for A: "))]
    
# for b in range(m):
#     B[b:b+1] = [int(input("Enter element for B: "))]
    
# print(A)
# print(B)

# max_A = max(A)
# max_B = max(B)

# index_of_max_A = A.index(max(A))
# index_of_max_B = B.index(max(B))

# A[index_of_max_A] = max_B
# B[index_of_max_B] = max_A

# print(A)
# print(B)

# # Task 6
# n = int(input("Number of students in A: "))

# A = []

# for a in range(n):
#     A[a:a+1] = [float(input("Enter average score: "))]

# max_A = max(A)
# index_of_max_A = A.index(max_A) + 1

# min_A = min(A)
# index_of_min_A = A.index(min_A) + 1

# print(f"The best student is student No.{index_of_max_A} with average {max_A}")
# print(f"The worst student is student No.{index_of_min_A} with average {min_A}")

# Task 7
# n = int(input("Number of elements in A: "))

# A = []

# for a in range(n):
#     A[a:a+1] = [int(input("Enter element: "))]

# print(A)

# min_A = min(A)

# for i in A[:]:
#     if i == min_A:
#         A.remove(i)

# print(A)

# Task 8
# n = int(input("Number of elements in A: "))
# average = float(input("Enter average score: "))

# A = []

# for a in range(n):
#     A[a:a+1] = [float(input("Enter scores: "))]
    
# print(A)

# index_of_max_A = A.index(max(A))

# A.insert(index_of_max_A + 1, average)

# print(A)

# Task 9
# n = int(input("Number of judges: "))

# J1 = []
# J2 = []
# J3 = []

# for i in range(n):
#     J1[i:i+1] = [int(input("Enter score for athlete 1: "))]

# for i in range(n):
#     J2[i:i+1] = [int(input("Enter score for athlete 2: "))]
    
# for i in range(n):
#     J3[i:i+1] = [int(input("Enter score for athlete 3: "))]
    
# Athletes = []

# average_of_J1 = float((sum(J1) - (max(J1) + min(J1))) / (n - 2))
# average_of_J2 = float((sum(J2) - (max(J2) + min(J2))) / (n - 2))
# average_of_J3 = float((sum(J3) - (max(J3) + min(J3))) / (n - 2))

# Athletes.extend([average_of_J1, average_of_J2, average_of_J3])

# print(Athletes)
