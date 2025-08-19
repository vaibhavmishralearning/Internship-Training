import calendar

year = int(input("Enter the year : "))


print("Year Calendar : \n")

calendar_display = calendar.calendar(year)
print(calendar_display)



# calendar.month() 
# calendar.calendar() - full year calendar
# calendar.isleap()
# calendar.weekday(year,month,day)
# calenday.leapdays()