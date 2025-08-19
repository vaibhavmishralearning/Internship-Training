print("Question 8 : Write a Program in Python using Loop to calculate combination\n")


def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact


n = int(input("Enter the value of n : "))
r = int(input("Enter the value of r : "))

combination = (factorial(n))/(factorial(r)*factorial(n-r))
print(f" {n} C {r} =  {combination}")