f_read=open("C:\Users\ABI\Desktop\PythonJuneWorks\python\FILE PROGRAMS\years.txt","r")
f_century_year=open("C:\\Users\\ABI\\Desktop\\PythonJuneWorks\\FILE PROGRAMS\\century.txt","w")
f_non_century_year=open("C:\\Users\\ABI\\Desktop\\PythonJuneWorks\\FILE PROGRAMS\\non century.txt","w")

for year in  f_read:

    y=int(year.rstrip("\n"))

    if y%100==0:

        f_century_year.write(str(y)+"\n")

    else:

        f_non_century_year.write(str(y)+"\n")