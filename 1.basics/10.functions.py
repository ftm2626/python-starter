def hello(name):
    print("It's me!" ,name)

hello("jasi")



# keyword arguments : arguments proceded by an identifier when we pass them to a function, the order doesn't matter

def func(first,second):
    return first + second

print(func(second="hunt",first="jasmine"))

# *args: parameter that will pack all arguments into a tuple, usefull so that a function can accept a varying amount of arguments

def func2(*args):
    sum = 0
    for i in args:
        sum += i 
    print(sum)


func2(4,6,7)

# **kwargs: parameter that will pack all arguments into a dictionaty, useful so that a function can accept a varying amount of keyword argument

def func3(**kwargs):
    print("hello" + kwargs["first"] + kwargs["last"])

func3(last="hunt",first="jasmine")
