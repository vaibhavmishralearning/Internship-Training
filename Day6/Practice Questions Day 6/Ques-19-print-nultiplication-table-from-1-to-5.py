print("Question 19 : Write a Program in Python using Loop to print multiplication table from 1 to 5\n")

for i in range(1,6):
    print(f"Multiplication Table of {i} is :")
    for j in range(1,11):
        print(f"  {i} x {j} = {i*j}")
    print()