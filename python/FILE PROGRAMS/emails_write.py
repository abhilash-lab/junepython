

email_ids=[
    "abcd@gmail.com",
    "bcde@gmail.com",
    "will@gmail.com",
    "bill@gmail.com",
    "gill@gmail.com"
]
f=open("C:\\Users\\ABI\\Desktop\\PythonJuneWorks\\FILE PROGRAMS\\email.txt","w")

for email in email_ids:

    f.write(email+"\n")