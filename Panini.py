city = ("Kharkiv", "Ukraine", 49.9935, 36.2304)
print(city[1])
print(city[3])
print(type(city))
name, country, latitude, longitude = city
print(name)
print(country)
city_list = list(city)
city_list[1] = "Poland"
city = tuple(city_list)
print(city)