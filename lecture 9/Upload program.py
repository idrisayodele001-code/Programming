# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#  Task 1
# import numpy as np
# sar = []
# n = int(input("enter the amount of elements: "))
# for i in range(n):
#  el = int (input("Enter number:\n"))
#  sar.append(el)
# print("Entered:")
# print(sar)
# print("Numpy:")
# arr = np.array (sar, int)
# print(arr)

# Task 2
# import numpy as np
# mas = np.array([[3, 6, 9, 12], [15, 18, 21, 24], [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60], [88, 11, 66,
# 77]])
# print(mas)
# new = mas[1::2,::2]
# print(new)


# task 3
# import numpy as np
# naujas = np.ones((10, 10))
# naujas[1:-1, 1:-1] = 0
# print(naujas)

# Task 4
# import numpy as np
# sarX = []
# sarY = []
# n = int(input("How many elements: "))
# for i in range(n):
#  x = int (input("Enter number for x:\n"))
#  sarX.append(x)
#  y = int (input("Enter number for y:\n"))
#  sarY.append(y)
# masX=np.array(sarX)
# print(masX)
# masY=np.array(sarY)
# print(masY)
# masZ = 5* np.subtract(masX,masY) + np.sin(masX) - 1/2 * np.cos(masY)
# print(np.round(masZ,3))

# Task 5
# import numpy as np
# import numpy as np
# array=np.zeros(10)
# print("An array of 10 zeros:")
# print(array)
# array1=np.ones(10)
# print("An array of 10 ones:")
# print(array1)
# array2=np.ones(10)*5
# print("An array of 10 fives:")
# print(array2)
# a=np.concatenate((array,array1,array2))
# print(a)

# Task 6
# import numpy as np
# arr1=np.arange(30,71)
# print("Integers from 30 to 70")
# print(arr1)
# arr2=np.arange(30,71,2)
# print("Even integers from 30 to 70")
# print(arr2)

# Task 7
# import numpy as np
# arr= np.arange(10,22).reshape((3, 4))
# print(arr)

# Task 8
# import numpy as np
# arr1 = np.array([0, 10, 20, 40, 60])
# print("Array 1: ",arr1)
# arr2 = [0, 40]
# print("Array 2: ",arr2)
# print("Comparison of each element:")
# print(np.in1d(arr1, arr2))



# task 9
# import numpy as np
# arr1 = np.array([0, 10, 20, 40, 60])
# print("Array 1: ",arr1)
# arr2 = [10, 30, 40]
# print("Array 2: ",arr2)
# print("Common values two arrays:")
# print(np.intersect1d(arr1, arr2))

# task 10
# import numpy as np
# arr = np.array([10, 10, 20, 20, 30, 30])
# print("Array:")
# print(arr)
# print("Unique elements:")
# print(np.unique(arr))
# matr = np.array([[1, 1], [2, 3]])
# print("Matrix:")
# print(matr)
# print("Unique elements in matrix:")
# print(np.unique(matr))


# task 11
# import numpy as np

# arr1 = np.array([[10,20,30], [40,50,60]])
# arr2 = np.array([[100], [200]])
# arr3 = np.append(arr1, arr2, axis=1)
# print (arr3)

# arr1 = np.array([[10,20,30], [40,50,60]])
# arr2 = np.array([[100,200,300]])
# arr3 = np.append(arr1, arr2, axis=0)
# print (arr3)
 
# task 12
# import numpy as np
# num = np.arange(36)
# arr = np.reshape(num, [4, 9])
# print("Array:")
# print(arr)
# sum = arr.sum(axis=0)
# print("\nColumns sums:")
# print(sum)
