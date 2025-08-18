print("\n__Grading System________________________\n")

marks = int(input("Enter Your Marks : "))

print("\nYOUR GRADE:")
if (marks < 0 or marks > 100):
    print("Invalid Input")
elif (marks >=0 and marks <= 40):
    print("You are Fail")
elif (marks >=41 and marks <= 50):
    print("C Grade")
elif (marks >=51 and marks <= 65):
    print("B Grade")
elif (marks >=66 and marks <= 80):
    print("A Grade")
elif (marks >=81 and marks <= 95):
    print("A++")
elif (marks >=96 and marks <= 100):
    print("Outstanding!!")

    
    
