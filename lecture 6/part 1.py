##tASK 1
##file = open("data.txt")
##file2 = open("res1.txt", "w")
##
##for line in file:
##     line = line.replace("v", "V")
##    
##     file2.write(line)
##
##file.close()
##file2.close()

## task 2   
##file = open("data.txt")
##file1 = open("res2.txt", "a")
##
##count = 0
##A = []
##
##for line in file:
##     amount = line.count("a") + line.count("A")
##    
##     A.append(amount)
##
##for line in A:
##     file1.write(str(line) + " ")
##
##file.close()
##file1.close()

##TASK 3
##file = open("data.txt")
##file1 = open("res3.txt", "w")
##
##A = []
##
##for line in file:
##     amount = line.count(" ") + line.count(",") + line.count(".")
##    
##     A.append(amount)
##
##for line in A:
##     file1.write(f"{A.index(line) + 1} line: {str(line)} symbols\n")
##
##file.close()
##file1.close()

##TASK 4
##data = open("reg_data1.txt").readlines()
##
##months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
##
##women = []
##men = []
##
##for line in data[1:]:
##     if line.startswith("3") or line.startswith("5"):
##         men.append(line)
##     elif line.startswith("4") or line.startswith("6"):
##         women.append(line)
##
##oldest_woman = min(women) if women else "No woman in list"
##oldest_man = min(men) if men else "No man in list"
##        
##print(f"The oldest woman was born: {months[int(oldest_woman[3:5]) - 1]} {oldest_woman[5:7]}, {19 if oldest_woman[0] == "4" else 20}{oldest_woman[1:3]}" if oldest_woman != "No woman in list" else "No woman in list")
##print(f"The oldest man was born: {months[int(oldest_man[3:5]) - 1]} {oldest_man[5:7]}, {19 if oldest_man[0] == "3" else 20}{oldest_man[1:3]}" if oldest_man != "No man in list" else "No man in list")
