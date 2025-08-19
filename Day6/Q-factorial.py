
print("\n_Factorial Of A Number__________________\n")

num = int(input("Enter A Number : "))
factorial = 1

for i in range(1,num+1):
    factorial = factorial * i

print("Factorial of", num,"is :",factorial)
print()