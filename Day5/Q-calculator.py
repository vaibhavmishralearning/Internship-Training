
print("\n__Calculator____________________________\n")


num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
operator = input("Enter Operators : ").strip()
print()

if operator == '+':
    result = num1 + num2
    print("Addition : ",result)
elif operator == '-':
    result = num1 - num2
    print("Subtraction : ",result)
elif operator == '/':
    result = num1 / num2
    print("Division : ",result)
elif operator == '*':
    result = num1 * num2
    print("Multiplication : ",result)
elif operator == '%':
    result = num1 % num2
    print("Modulus : ",result)
elif operator == '//':
    result = num1 // num2
    print("Floor Division : ",result)
elif operator == '**':
    result = num1 ** num2
    print("Exponentiation : ",result)
else:
    print("Invalid Choice")