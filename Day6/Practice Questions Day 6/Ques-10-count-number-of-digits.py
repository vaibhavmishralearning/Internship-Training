print("Question 10 : Write a Program in Python using Loop to count number of digits in a number\n")

count_digit = 0

num = int(input("Enter any number : "))
n = num

while n > 0:
    count_digit += 1
    n = n // 10

print(f"Number of digits in {num} is : {count_digit}")
