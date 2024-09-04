# print all the non_century yrs frm 1800 to2024 

year=1800

for i in range(1800,2025):
    if(year%100!=0):
        print(year)
    year=year+1
