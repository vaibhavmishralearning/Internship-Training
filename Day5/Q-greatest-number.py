print("\n__Greatest Of Three Numbers_____________________________________\n")

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number : "))

print()
if (num1 > num2):
    if (num1 > num3):
        print(num1,"is the Greatest Number\n")
    else:
        print(num3,"is the Greatest Number\n")
else:
    if (num2 > num3):
        print(num2,"is the Greatest Number\n")
    else:
        print(num3,"is the Greatest Number\n")