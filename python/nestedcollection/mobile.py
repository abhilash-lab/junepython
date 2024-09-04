mobiles=[
    {"id":100,"title":"s23 ultra","brand":"samsung","price":1250000,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]
#print mobile names
mobile_names=[mob.get("title")for mob in mobiles]
#print(mobile_names)

#print all mobile brands
brand_names=[mob.get("brand")for mob in mobiles]
#print(brand_names)

#print samsung mobiles names
samsung_mob=[mob.get("title")for mob in mobiles if mob.get("brand")=="samsung"]
#print(samsung_mob)

#print 40000 to 23000  range mobiles
range=[ mob.get("title")for mob in mobiles if mob.get("price") in range(23000,40000+1)]
#print(range)

#print higest priced mobile name
# high_price=max([mob.get("price") for mob in mobiles])
# costly_mobile=[mob.get("title")for mob in mobiles if mob.get("price")==high_price]
# print(costly_mobile)

#function call 
def get_price(mob):
    return mob.get("price")
costly_mobile=max(mobiles,key=get_price)
#print(costly_mobile)
chepest_mobile=min(mobiles,key=get_price)
#print(chepest_mobile)

#print total price of all mobiles
total=sum( mob.get("price")for mob in mobiles)
#print(total)

sort=sorted(mobiles,key=get_price,reverse=True)
print(sort)
