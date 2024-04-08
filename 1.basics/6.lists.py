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


student = [("fatemeh","A",26),
           ("zahra","C",27),
           ("mohsen","A",25),
           ("ali","F",28),
           ("reza","B",30),]

grade = lambda grades:grades[1]

student.sort(key=grade)

for i in student:
    print(i)


# list comprehensions : a way to create a new list with less syntax, can mimic certain lambda function, easier to read
# list = [expression fo items in iterable if conditional]

# squares = []                  # create an empty list
# for i in range(1,11):         # create a for loop
#     squares.append(i*i)       # define what each loop interation should do
# print(squares)


squares = [i * i for i in range(1,11)] #list comprehention

print(squares)

grades = [100,90,80,70,60,50,40,30,20,10]
# passed_students = list(filter(lambda x:x >=60,grades))
# passed_students = [i for i in grades if i >= 60] #list comprehention
passed_students = [i if i >= 60 else "Failed" for i in grades] #list comprehention

print(passed_students)