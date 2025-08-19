


def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
        return True
    else:
        return False


print("\n__Check Leap Year______________________\n")
year = int(input("Enter The Year : "))
isLeapYear = check_leap_year(year)

if (isLeapYear):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")