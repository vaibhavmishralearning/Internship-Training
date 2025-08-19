print("Question 17 : Write a Program in Python using Loop to find sum of odd numbers between 1 and 50\n")

sum_odd = 0

for i in range(1,51):
    if i % 2 != 0:
        sum_odd += i

print(f"Sum of odd numbers from 1 to 50 : {sum_odd}")