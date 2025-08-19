
print("\n_Reversed Pattern ____________ \n")
num = int(input("Enter a number : "))
for i in range(num,0,-1):
    for j in range(num, 0,-1):
        print(i,j)
    print()