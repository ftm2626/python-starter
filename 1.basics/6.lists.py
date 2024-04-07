food = ["pizza","burger","hotdog","pudding","pasta"]

food[0] = "sushi"
food.append("ice cream")
food.remove("pudding")
food.pop()
food.insert(2,"cake")
food.sort()
food.clear()

# print(food)

# 2D lists : list of lists   
drinks = ["coffee","water","tea"]
dinner = ["pizza","burger","hotdog"]
dessert = ["cake","pudding"]
all_food = [drinks, dinner, dessert] 

# print(all_food[0][0])


# sort

drinks.sort()
drinks.sort(reverse=True)

for i in drinks:
    print(i)