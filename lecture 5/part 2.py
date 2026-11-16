## Task 1
##line = input("Enter string: ").strip()
##print(line)
##letter = input("Enter letter to count: ").strip()
##print(line.count(letter))

# Task 2
# line = input("Enter string: ").strip()

# counts = []

# for number in range(10):
#     counts.append(line.count(str(number)))
#     print(f"{number}: {counts[number]}")

# print(f"{counts.index(max(counts))} repeated the most with {max(counts)} repeat")

# Task 3
# line = input("Enter string: ").strip()
# print(f"Word Kaunas is repeated {line.lower().count("kaunas")} times")

# Task 4
# line = input("Enter string: ").strip()
# line1 = line.replace("kaunas", "Vilnius")
# line1 = line1.replace("Kaunas", "Vilnius")
# line1 = line1.replace("KAUNAS", "Vilnius")
# print(line1)

# Task 5
# line = input("Enter string: ").strip()

# words = line.split(" ")

# letters = []

# for word in range (len(words)):
#     letters.append(0)
#     for letter in range(len(words[word])):
#         letters[word] += 1
    
# index_of_max = letters.index(max(letters))
# longest = words[index_of_max]

# line_new = line.replace(longest, "")

# print(line_new)

# Task 6
# import re

# line = input("Enter string: ").strip()

# signs = "\\ |\\,|\\;"

# words = re.split(signs, line)

# print(words)

# words_amount = {}

# for word in words:
#     if not word in words_amount:
#         words_amount[word] = 1
#     else:
#         words_amount[word] += 1

# print(words_amount)
