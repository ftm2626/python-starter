# reduce : apply a function to an iterable and reduce it to a single cumulative value. performs function on first two elements and repeates process until one value remains.

# reduce(function, iterable)

import functools

letters = ["H","E","L","L","O"]
# proccess
# letters = ["HE","L","L","O"]
# letters = ["HEL","L","O"]
# letters = ["HELL","O"]
# letters = ["HELLO"]

reduce_func = lambda x , y: x + y
word = functools.reduce(reduce_func,letters)
print(word)

factorial = [1,2,3,4,5]
factoral_func = lambda x,y:x*y
number = functools.reduce(factoral_func,factorial)

print(number)

# 5:11:00