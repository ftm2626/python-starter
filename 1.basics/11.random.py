import random
x= random.randint(1,6)
y=random.random() #random number between 0 and 1

my_list = ["rock","paper","scissors"]
z = random.choice(my_list)

order = [1,2,3,4,5,6,7,8,9]
random.shuffle(order)

print(order)