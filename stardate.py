#!/usr/bin/python3

from datetime import datetime

now = datetime.now()
year = now.year
day_of_year = now.timetuple().tm_yday
hour = now.hour
minute = now.minute
second = now.second

one_hour = 1 / 24 / 365
one_minute = one_hour / 60
one_second = one_minute / 60

exact_day = (day_of_year / 365)
exact_hour = hour * one_hour
exact_minute = now.minute * one_minute
exact_second = now.second * one_second
exact_decimal = exact_day + exact_hour + exact_minute + exact_second
decimal = float('%.8f'%(exact_decimal))
#error = decimal * 365 - day_of_year - (hour / 24)
#error_hours = error * 24
stardate = year + decimal

#print("stardate for", year, day_of_year, hour)
#print("error:", error, "in hours:", error_hours)
print(stardate)
