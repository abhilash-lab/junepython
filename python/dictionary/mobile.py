#create a dictionary mobile with keys name ,brand,price, is_available
#add a key : value to the dictionary offer:500

mobile={"name":"iphone","brand":"apple","price":50000,"is_available":True}

#print mobile name 
# print(mobile.get("name"))
# for k ,v in mobile.items():
   # print(k,v)
    
mobile["offer"]=500
if "offer" in mobile:
    selling_price=mobile.get("price")-mobile.get("offer")
    print(selling_price)
else:
    print(mobile.get("price"))




