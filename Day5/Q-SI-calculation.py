print()
print("__Simple Interest Calculation _______________________")
print()

principle_amount = int(input("Enter Your Principle Amount : "))
time = float(input("Enter Time Duration : "))
rate_interest = float(input("Enter Rate Of Interest : "))

SI = ( principle_amount * rate_interest * time ) / 100

print()
print("Simple Interest : ",SI)
print()
