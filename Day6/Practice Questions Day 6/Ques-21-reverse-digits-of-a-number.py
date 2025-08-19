print("Question 21 : Write a Program in Python using Loop to reverse the digits of a numberr\n")

num = int(input("Enter any number : "))
print(f"\nEntered Number is : {num}")

num_rev = 0

while num > 0:
    rem = num % 10
    num_rev = num_rev*10 + rem
    num = num // 10

print(f"Reversed Number is : {num_rev}")
