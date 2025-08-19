print("Question 4 : Write a Program in Python using Loop to find power of a number\n")


base = int(input("Enter base number : "))
raise_to = int(input("Enter power of number : "))

num_pow = 1

for i in range(1, raise_to+1):
    num_pow = num_pow * base

print(f"  {base} ^ {raise_to} = {num_pow}")