print("Question 7 : Write a Program in Python using Loop to check if the number is palindrome\n")


num = int(input("Enter any number : "))
num_rev = 0
n = num

while n > 0:
    rem = n % 10
    num_rev = num_rev * 10 + rem
    n = n // 10

if num_rev == num:
    print("This is a palindrome number")
else:
    print("This is not a palindrome number")