employee={"name":"hari","dept":"r&d","salary":50000,"combo_offer":1000,"extra_wrking_days":30}


# print all keys and values


# for k,v in employee.items():
#     print(k,v)

# print net pay
if "extra_wrking_days" in employee:
    net_pay=employee.get("salary")+employee.get("combo_offer")*employee.get("extra_wrking_days")
    print(net_pay)
else:
    print(employee.get("salary"))



