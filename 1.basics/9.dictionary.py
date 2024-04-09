# dictionary: a changeable, unordered collection of unique key:value pairs, fat because the use hashing, allows us to access a value quickly

capitals = {
    "USA":"DC",
    "India":"Dehli",
    "China":"Beijing",
    "Russia":"Mascow"
}

get_capital = capitals["Russia"] 
# get_capital = capitals[3] -> does NOT work, no numbers
# get_capital = capitals["Iran"] -> Error 
get_capital2 =capitals.get("Iran") #None
get_keys = capitals.keys()
get_values = capitals.values()
get_all = capitals.items()

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"LA"})
capitals.pop("China")
capitals.clear()


for key,value in capitals.items():
    print(key,value)


# dictionary comprehension : create dictionaris using an expression, can replace for loops and certain lambda functions

# dictionary = {key: expression for (key, value) in iterable}

cities_in_f = {'new york':32 , "boston" : 75, "los aangeles":100, "chicago":50}
cities_in_C = {key:round((value-32)*(5/9)) for (key,value) in cities_in_f.items()}
print(cities_in_C)

weather = {'new york':"snowing" , "boston" : "sunny", "los aangeles":"sunny", "chicago":"cloudy"}
sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}

print(sunny_weather)