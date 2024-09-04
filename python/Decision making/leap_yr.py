# pgrm to find given yr is leap yr
# read the yr frm the user

year=int(input("Enter the year "))
if(year%100==0 and year%400==0) or  (year%100!=0 and year%4==0):
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")