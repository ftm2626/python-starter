# map : applies a function to each item in an iterable (list, tuple, etc)

# map(function, iterable)

store = [
    ("shirts",20.00),
    ("pants",25.00),
    ("jacket",50.00),
    ("socks",10.00),
]

to_euros = lambda data: (data[0],data[1]*0.82)

store_euros = list(map(to_euros,store))

for i in store_euros:
    print(i)


# filter : creates a collection of elements from an iterable for which a function returns true

# filter(function, iterable)

friends = [
    ("Rachel",19),
    ("Monica",18),
    ("Phoebe",17),
    ("Joey",16),
    ("Chandler",21),
    ("Ross",20  ),
]

age = lambda data: data[1] >= 18

can_vote = list(filter(age,friends))

for i in can_vote:
    print(i)