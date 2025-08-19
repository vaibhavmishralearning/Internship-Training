print("Question 20 : Write a Program in Python using Loop to check if the number is a prime number or not\n")


num = int(input("Enter any number : "))
isPrime = True

for i in range(2,int(num/2)+1):
    if num % i == 0:
        isPrime = False

if isPrime:
    print("Number is a prime number.")
else:
    print("Number is not a prime number.")
    