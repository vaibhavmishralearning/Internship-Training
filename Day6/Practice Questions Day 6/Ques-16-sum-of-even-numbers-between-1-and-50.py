print("Question 16 : Write a Program in Python using Loop to find sum of even numbers between 1 and 50\n")

sum_even = 0

for i in range(1,51):
    if i % 2 == 0:
        sum_even += i

print(f"Sum of even numbers from 1 to 50 : {sum_even}")