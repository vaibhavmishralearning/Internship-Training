
def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def menu():
    print("\n\t_____ Arithmetic Operations _____")
    print("\n Select Operation to perform : \n\t1. Addition\n\t2. Subtraction\n\t3. Multiplication\n\t4. Division")

while True:
    menu()
    choice = input("Enter Your Choice : ")
    print()
    if choice == '5':
        print("Exiting the program .......")
        break
    elif choice in ['1','2','3','4']:
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number : "))
        print()
        if choice == '1':
            result = addition(num1,num2)
            print(f"Addition : {result}")
        elif choice == '2':
            result = subtraction(num1,num2)
            print(f"Subtraction : {result}")
        elif choice == '3':
            result = multiply(num1,num2)
            print(f"Multiplication : {result}")
        elif choice == '4':
            result = divide(num1,num2)
            print(f"Divide : {result}")
    else:
        print("Invalid Input")
