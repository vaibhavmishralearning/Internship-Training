
print("Question 2 : Write a Program in Python using Loop to find Fibonacci Series\n")

num = int(input("Enter Number Of Terms : "))


if num == 1:
    print('0')
elif num > 1:
    first = 0
    second = 1
    print(first,second,end=' ')
    for i in range(3,(num+1)):
        third = first + second
        print(third,end=' ')
        first = second
        second = third
else:
    print("Invalid Input")

print()
print()