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
