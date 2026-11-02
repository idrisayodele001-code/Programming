##Question1
##def maximum(a, b, c):
##    if a >= b and a >= c:
##        return a
##    elif b >= a and b >= c:
##        return b
##    else:
##        return c
##
##
##print(maximum(10, 25, 7))

##Question 2
##def sum_list(numbers):
##    total = 0
##
##    for number in numbers:
##        total = total + number
##
##    return total
##
##
##print(sum_list([8, 2, 3, 0, 7]))


##Question 3
##def reverse_string(text):
##    return text[::-1]
##
##
##print(reverse_string("1234abcd"))
##

##Question 4

##def count_letters(text):
##    upper = 0
##    lower = 0
##
##    for char in text:
##        if char.isupper():
##            upper = upper + 1
##        elif char.islower():
##            lower = lower + 1
##
##    print("No. of Upper case characters:", upper)
##    print("No. of Lower case Characters:", lower)
##
##count_letters("The quick Brown Fox")

##question 5
##def is_perfect(number):
##    if number < 2:
##        return False
##
##    total = 0
##
##    for i in range(1, number):
##        if number % i == 0:
##            total = total + i
##
##    return total == number
##
##
##print(is_perfect(6))
##print(is_perfect(10))
##print(is_perfect(28))

##question 6
##def is_palindrome(text):
##    text = text.lower().replace(" ", "")
##    return text == text[::-1]
##
##
##print(is_palindrome("madam"))
##print(is_palindrome("hello"))
##print(is_palindrome("nurses run"))

##Question 7
##def sort_words(text):
##    words = text.split("-")
##    words.sort()
##    return "-".join(words)
##
##
##text = input("Enter words separated by hyphens: ")
##print(sort_words(text))


