
print()
print("__Average Marks Calculation _______________________")
print()

maths = float(input("Enter Your Maths Marks :"))
physics = float(input("Enter Your Physics Marks :"))
english = float(input("Enter Your English Marks :"))
computer = float(input("Enter Your Computer Marks :"))
chemistry = float(input("Enter Your Chemistry Marks :"))

total_marks = maths + physics + english + computer + chemistry
avg_marks = total_marks / 5

print()
print("Total Marks : ",total_marks)
print("Averange Of Five Subjects : ",avg_marks)