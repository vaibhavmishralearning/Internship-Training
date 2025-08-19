print("Question 3 : Write a Program in Python using Loop to find greatest common divisor\n")


num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

smaller_num = 0
hcf = 1

if num1 > num2:
    smaller_num = num2
else:
    smaller_num = num1

for i in range(1,smaller_num+1):
    if ((num1 % i == 0) and (num2 % i == 0)):
        hcf = i

print(f"Highest Common Factor of {num1} and {num2} = {hcf}")
