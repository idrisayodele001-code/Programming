##task 1
##m = int(input('Number of rows, m = '))
##n = int(input('Number of columns, n = '))
##
##matrix = []
##matrix1 = []
##matrix2 = []
##
##for i in range(0, m):
##    matrix += [0]
##    matrix1 += [0]
##    matrix2 += [0]
##
##
##for i in range(0, m):
##    matrix[i] = [0] * n
##    matrix1[i] = [0] * n
##    matrix2[i] = [0] * n
##
##
##for i in range(0, m):
##    for j in range(0, n):
##        print('Matrix1 entry in row:', i+1, 'column:', j+1)
##        matrix[i][j] = int(input())
##
##        print('Matrix2 entry in row:', i+1, 'column:', j+1)
##        matrix1[i][j] = int(input())
##
##        matrix2[i][j] = matrix[i][j] + matrix1[i][j]
##
##
##print("First matrix:", matrix)
##print("Second matrix:", matrix1)
##print("Sum of matrices:", matrix2)

##question 2
##m = int(input("Number of rows: "))
##n = int(input("Number of columns: "))
##
##matrix = []
##
##for i in range(0, m):
##    matrix += [0]
##
##for i in range(0, m):
##    matrix[i] = [0] * n
##
##for i in range(0, m):
##    for j in range(0, n):
##        print("Enter number in row:", i+1, "column:", j+1)
##        matrix[i][j] = int(input())
##
##for i in range(0, m):
##    for j in range(0, n):
##        if i == j:
##            matrix[i][j] = 0
##        elif i + j == n - 1:
##            matrix[i][j] = 0
##
##print("Result:")
##
##for r in matrix:
##    for c in r:
##        print(c, end=" ")
##    print()

##question 3
##m = int(input("Number of students: "))
##n = int(input("Number of grades: "))
##
##STUD = []
##AVG = []
##
##for i in range(0, m):
##    STUD += [0]
##
##for i in range(0, m):
##    STUD[i] = [0] * n
##
##for i in range(0, m):
##    for j in range(0, n):
##        print("Enter grade for student:", i+1, "grade:", j+1)
##        STUD[i][j] = float(input())
##
##for i in range(0, m):
##    AVG += [0]
##
##for i in range(0, m):
##    total = 0
##    for j in range(0, n):
##        total = total + STUD[i][j]
##
##    AVG[i] = total / n
##
##print("Student grades:", STUD)
##print("Average grades:", AVG)
