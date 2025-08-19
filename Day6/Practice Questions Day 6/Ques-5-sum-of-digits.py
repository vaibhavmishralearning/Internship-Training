print("Question 5 : Write a Program in Python using Loop to find sum of digits of a number\n")


num = int(input("Enter any number : "))
n = num

sum_digits = 0

while n > 0:
    digit = n % 10
    sum_digits = sum_digits + digit
    n = n // 10

print(f"Sum of digits of {num} is : {sum_digits}")