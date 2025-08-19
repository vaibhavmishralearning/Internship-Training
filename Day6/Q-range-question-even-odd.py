


print("\nPrinting Range _____________________\n")

num = int(input("Enter Number Of Terms : "))

print("\nAll Even Numbers Till ",num,":")
for i in range(1,num + 1):
    if i % 2 == 0:
        print(i)

print("\nAll Odd Numbers Till ",num,":")
for i in range(1,num + 1):
    if i % 2 != 0:
        print(i)
print()