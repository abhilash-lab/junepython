#find the count the expenses
#print(expenses_count)
#print all expenses
#print expenses >15000
#print total expenses
#print avarage expenses 

expenses=[12000,13000,11000,14000,15000,21000,22000,13000]
sum=0
print(expenses)
expense_count=len(expenses)
print(expense_count)
for i in range (0,expense_count):
    if expenses[i]>15000:
        print(expenses[i])

    sum=sum+expenses[i]
        
print(sum)

average=sum/expense_count
print(average)

