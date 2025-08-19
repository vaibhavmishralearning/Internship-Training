print("Question 6 : Write a Program in Python using Loop to find reverse of a number\n")


num = int(input("Enter any number : "))
n = num

num_rev = 0

while n > 0:
    rem = n % 10
    num_rev = num_rev * 10 + rem
    n = n // 10

print(f"Reversed Number is : {num_rev}")