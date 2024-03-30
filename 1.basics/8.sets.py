# set: a collection which is unordered, unindexed, no duplicated values
# a set is faster than a list


utensils = {"fork","spoon","knife","knife","knife"}
dishes = {"bowl","plate","cup","knife"}

for x in utensils:
    print(x)  # it does not print in order, only print knife once!
    
utensils.add("napkin")
utensils.remove("spoon")
dinner_table = utensils.union(dishes)
utensils_has_dish_doesnt = utensils.difference(dishes)
utensils.clear()
utensils.update(dishes)


