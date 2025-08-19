
def check_even(num):
    return num % 2 == 0



while True:
    print("\n__Check Even Or Odd_________________\n")
    print("\t1. Check\n\t2. Exit\n")

    choice = input("Enter your choice : ")
    print()
    if choice == '1':
        num = int(input("Enter a number : "))
        result = check_even(num)
        if result:
            print(f"{num} is a even number.")
        else:
            print(f"{num} is a odd number")
    elif choice == '2':
        print("Exiting the program.")
        break
    else:
        print("Invalid Input.")