import datetime

current = datetime.datetime.now()
print("Current Date and Time : ",current)

now = datetime.datetime.now()
print("Current Time : ",now.time())

today = datetime.date.today()
print("Today's Date : ",today)

my_date = datetime.date(2025,6,21)
print("Custom Date : ",my_date)

print("Formatted Date : ",now.strftime("%d-%m-%y"))
print("Formatted Date : ",now.strftime("%H:%M:%S"))