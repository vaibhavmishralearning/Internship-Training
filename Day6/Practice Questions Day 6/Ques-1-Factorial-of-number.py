
    

print("Question 1 : Write a Program in Python using Loop to find Factorial of a number\n")

num = int(input("Enter a number : "))
factorial = 1
for i in range(1,num+1):
    factorial = factorial * i
print(f"Factorial of {num} is {factorial}.\n")