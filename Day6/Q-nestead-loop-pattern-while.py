


num = int(input("Enter A Number : "))
print()
count1 = 1
count2 = 1
while count1 <= num:
    count2 = 1
    while count2 <= num:
        print(count1,count2)
        count2 += 1
    print()
    count1 += 1
