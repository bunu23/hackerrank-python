# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar


input_date = input()
month, day, year = map(int, input_date.split())


day_of_week = calendar.weekday(year, month, day)

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]


print(days[day_of_week])
