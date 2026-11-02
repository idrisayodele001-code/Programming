##Question 1
##def from_file(fv):
##    f = open(fv)
##    num = []
##
##    lines = f.readlines()
##
##    for line in lines:
##        number = int(line)
##        num.append(number)
##
##    f.close()
##    return num
##
##
##def del_elements(arr):
##    new_arr = []
##
##    for number in arr:
##        if len(new_arr) == 0 or number > new_arr[-1]:
##            new_arr.append(number)
##
##    return new_arr
##
##
##numb = from_file("data_num.txt")
##
##print("These numbers are in the file:")
##print(numb)
##
##in_order = del_elements(numb)
##
##print("Ordered numbers:")
##print(in_order)
##

##Question 2
##def from_file(fv):
##    f = open(fv)
##    num = []
##
##    lines = f.readlines()
##
##    for line in lines:
##        number = int(line)
##        num.append(number)
##
##    f.close()
##    return num
##
##
##def print_array(arr):
##    print(arr)
##
##
##def del_one(arr, ind):
##    del arr[ind]
##    return arr
##
##
##def del_all(arr):
##    i = 0
##
##    while i < len(arr) - 1:
##        if arr[i] == arr[i + 1]:
##            del_one(arr, i + 1)
##        else:
##            i = i + 1
##
##    return arr
##
##
##numb = from_file("new 1.txt")
##
##print("Array A before deleting:")
##print_array(numb)
##
##numb = del_all(numb)
##
##print("Array A after deleting equal elements:")
##print_array(numb)

##Question 3
##def from_file(fv):
##    f = open(fv)
##    num = []
##
##    lines = f.readlines()
##
##    for line in lines:
##        number = int(line)
##        num.append(number)
##
##    f.close()
##    return num
##
##
##def print_array(arr):
##    print(arr)
##
##
##def where_to_add(arr, x):
##    i = 0
##
##    while i < len(arr) and arr[i] <= x:
##        i = i + 1
##
##    return i
##
##
##def add_all(arr, place, x, k):
##    for j in range(k):
##        arr.insert(place + j, x)
##
##    return arr
##
##
##numb = from_file("number 1.txt")
##
##print("Array B before adding:")
##print_array(numb)
##
##x = int(input("Enter element to add: "))
##k = int(input("Enter how many times: "))
##
##place = where_to_add(numb, x)
##
##numb = add_all(numb, place, x, k)
##
##print("Array B after adding:")
##print_array(numb)
##
