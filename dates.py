from datetime import *

d  = date.today()
print(d)

December = date(1998,5,15)
print(December)

# time showing 9:45

time = time(21,45,35)
print(time)

appiontment = datetime(2005,6,16,16,15)
print(appiontment)
print(datetime(2015,4,19))


## parsing dates and times and date-times combined

Bonfire_team  = datetime.strptime("5/11/2001 15:30","%d/%m/%Y %H:%M")
print(Bonfire_team)

d = datetime.strptime("5/01/2001","%d/%m/%Y")
print(d)
print(date(2001,5,2))

## code that prompts user to input date
# while True:
#   user = input("Input date the date in the form (d/m/y)")
#   try:
#     user_parsed = datetime.strptime(user,"%d/%m/%Y")
#     print("Date of birth:",user_parsed)
#     print("Sucessful")
#     break

#   except TypeError:
#     print("Try again")


## We can also format dates to the format we want

inputt  = input("Enter date")
inputtt = datetime.strptime(inputt,"%d-%m-%Y")
print(inputt)
birthday = datetime(2001,1,16,11,30)
print(birthday.strftime("%c"))


today = datetime.now()
print(today.strftime("%A %B %d %Y (%H:%M:%S %p)"))

# Spans of time(calculating time between dates)
from datetime import timedelta
a = timedelta(weeks= 3,days=4,hours=9)
in_the_future = datetime.now() + a
print(in_the_future)
in_the_future = in_the_future.strftime("%B %d %Y (%H:%M)")
print(in_the_future)

b = timedelta(days=7)
christmas = date(2017,12,25)
one_week_after = christmas + b
h = one_week_after.strftime("%d %B %Y")
print(h)

## calculating time left 
end_of_the_month = date(2021,3,31)
time_left = end_of_the_month - date.today()
print(time_left.days,"Days left")



dd = datetime.now()
lol = date(2003,5,17)
print(lol.strftime("%A %B %d %Y"))
print(dd.strftime("%B %d %Y"))

##Parsing some more 
my_day = input("Enter you birthday in the form of (Y/M/D)")
my_days = datetime.strptime(my_day,"%Y/%m/%d")
print(my_days)

# span of time
# days till eid 

today = datetime.now()
Eid = datetime(2021,7,23,23,55)
days_left_till_eid = Eid - today
print(days_left_till_eid.days,"hours left")






























