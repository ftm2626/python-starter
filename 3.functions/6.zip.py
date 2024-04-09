# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each elements

usernames= ["dude","bro","mister"]
passwords = ("password","abc123","hello")

users = zip(usernames, passwords)


for i in users:
    print(i)