import calendar

year = int(input("Enter the year : "))
month = int(input("Enter the month : "))
day = int(input("Enter the day : "))

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


weekday_index = calendar.weekday(year,month,day)
print(f"The day on {day}-{month}-{year} is {days[weekday_index]}")