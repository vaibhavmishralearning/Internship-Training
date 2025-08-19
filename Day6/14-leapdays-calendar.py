
import calendar

year_start = int(input("Enter Starting year :"))
year_end = int(input("Enter Ending year :"))


no_of_leap_days = calendar.leapdays(year_start,year_end)

print(f"Number of leap days between {year_start} and {year_end} is {no_of_leap_days}")