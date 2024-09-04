f=open("C:\\Users\\ABI\\Desktop\\PythonJuneWorks\\FILE PROGRAMS\\student.txt","r")
student=[]
for stud in f:
    student.append(stud.rstrip("\n"))

print(student )
