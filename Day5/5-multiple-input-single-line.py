print()
print("__Multiple Inputs On Single Line ___________________________")
print()
num1 , num2 = map(int,input("Enter Two Numbers Separated By Space : ").split())

add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2

print()
print("First Number : ",num1)
print("Second Number : ",num2)
print()
print("Addition : ",add)
print("Subtraction : ",subtract)
print("Multiplication : ",multiply)
print("Division : ",divide)