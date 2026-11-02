##task 1
##import math
##
##matrix = []
##multiplications = []
##sums = []
##
##with open("matrix1.txt", "r") as f:
##     for line in f:
##         matrix.append(list(map(int, line.split())))
##
##for i, row in enumerate(matrix):
##     if (i + 1) % 2 == 0:
##         sums.append(sum(row))
##     else:
##         multiplications.append(math.prod(row))
##
##print(matrix)
##print(multiplications)
##print(sums)

##task 2
##matrix = []
##
##with open("matrix2.txt", "r") as f:
##     for line in f:
##         matrix.append(list(map(int, line.split())))
##
##print(matrix)        
##
##matrix_transpose = [[], [], [], []]
##
##for row in matrix:
##     matrix_transpose[0].append(row[0])
##     matrix_transpose[1].append(row[1])
##     matrix_transpose[2].append(row[2])
##     matrix_transpose[3].append(row[3])
##
##print(matrix_transpose)
##
##first_column_sum_new_matrix = sum(matrix[0])
##first_column_sum_former_matrix = sum(matrix_transpose[0])
##
##print(f"Sum of columns of first matrix: {first_column_sum_former_matrix}, Sum of columns of second matrix: {first_column_sum_new_matrix}")
##
##if first_column_sum_former_matrix > first_column_sum_new_matrix:
##     print("First is bigger")
##elif first_column_sum_new_matrix > first_column_sum_former_matrix:
##     print("Second is bigger")
##else:
##     print("They are equal")

##Task 3
##matrix = []
##
##with open("matrix3.txt", "r") as f:
##     for line in f:
##         matrix.append(list(map(int, line.split())))
##
##max_num = 0
##max_row = 0
##max_column = 0
##
##for i, row in enumerate(matrix):
##     if max(row) > max_num:
##         max_num = max(row)
##         max_row = i + 1
##         max_column = row.index(max(row)) + 1
##
##print(f"The largest number is {max_num} - in the {max_row} row and {max_column} column")
##
##task 4
##def read_file(filename):
##     matrix = []
##
##     with open(filename, "r") as f:
##         for line in f:
##             matrix.append(list(map(int, line.split())))
##
##     return matrix
##
##def min_each_row(matrix):
##     mins = []
##
##     for i, row in enumerate(matrix):
##         mins.append({
##             "value": min(row),
##             "row": i + 1,
##             "column": row.index((min(row))) + 1
##         })
##
##     max_of_mins = max(mins, key=lambda x: x["value"])
##
##     return mins, max_of_mins
##
##def print_matrix(matrix):
##     print(matrix)
##
##def print_mins(mins, max_of_mins):
##     print(f"Minimum value of each row in matrix and their position: {mins}")
##     print(f"Biggest of minimum values is {max_of_mins}")
##
##def main():
##     matrix = read_file("matrix4.txt")
##     mins, max_of_mins = min_each_row(matrix)
##     print_matrix(matrix)
##     print_mins(mins, max_of_mins)
##
##main()
