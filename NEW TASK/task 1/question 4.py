# Write  a program for grade classification based on percentage 
# conditions 
#   percentage = 90
#   grade A
#  percentage in between 80-90 
# grade B
# percentage in between 70-80 
# grade C 
# percentage less than 70 
# fail 

mark=int(input("enter the mark:"))

if mark>=90:
    print("A grade")

elif mark<90 and mark>=80:
    print("B grade")

elif mark<80 and mark>=70:
    print("C grade")

else:
    print("fail")