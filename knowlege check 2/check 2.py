##Question 1
##def read_data():
##    file = open("science.txt", "r")
##    scientists = file.readlines()
##    file.close()
##    return scientists
##
##
##def filter_data(scientists):
##    results = []
##
##    for line in scientists:
##        surname, name, science, personal_data = line.split()
##
##        if personal_data[0] in "34" and personal_data[1:3] == "89" and science == "physics":
##            results.append(surname + " " + name[0] + ". " + science)
##
##    return results
##
##
##def print_results(results):
##    file = open("PH_scientists.txt", "w")
##
##    file.write("Surname  N. Science\n")
##
##    for person in results:
##        file.write(person + "\n")
##
##    file.close()
##
##
##scientists = read_data()
##results = filter_data(scientists)
##print_results(results)
##
##print("Results saved successfully!")



##Question 2
##def sum_odd(numbers):
##    total = 0
##
##    for number in numbers:
##        if number % 2 != 0:
##            total = total + number
##
##    return total
##
##
##numbers = [2, 5, 7, 8, 10, 13, 15]
##
##result = sum_odd(numbers)
##
##print("The sum of odd numbers is:", result)



 
##Question 3
##def enter_data(m, n):
##    Weather = []
##
##    for i in range(m):
##        day = []
##        print("Enter temperatures for day", i + 1)
##
##        for j in range(n):
##            temp = float(input("Enter temperature: "))
##            day.append(temp)
##
##        Weather.append(day)
##
##    return Weather
##
##
##def calculate_average(Weather, m, n):
##    AVG = []
##
##    for i in range(m):
##        total = 0
##
##        for j in range(n):
##            total += Weather[i][j]
##
##        average = total / n
##        AVG.append(average)
##
##    return AVG
##
##
##def hottest_day(AVG):
##    hottest = 0
##
##    for i in range(len(AVG)):
##        if AVG[i] > AVG[hottest]:
##            hottest = i
##
##    return hottest + 1
##
##
##m = int(input("Enter number of days: "))
##n = int(input("Enter number of temperature measurements per day: "))
##
##Weather = enter_data(m, n)
##
##AVG = calculate_average(Weather, m, n)
##
##print("\nAverage temperatures:")
##
##for i in range(m):
##    print("Day", i + 1, ":", AVG[i])
##
##day = hottest_day(AVG)
##
##print("\nThe hottest day is day", day)
##print("Its average temperature is:", AVG[day - 1])
##
