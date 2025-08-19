print("Question 9 : Write a Program in Python using Loop to find lcm of two numbers\n")


num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

max_num = 0
if num1 > num2:
    max_num = num1
else:
    max_num = num2

lcm = 0

while True:
    if ( max_num % num1 == 0 and max_num % num2 == 0):
        break
    max_num = max_num + 1

print("Least Common Multiple (LCM) is : ",max_num)