#  higher order functions : a function that either : 1.acceptsa function as on argument, 2.returns a function (in python, functions are also treated as an object)

def loud(text):
    return text.upper()

def quite(text):
    return text.lower()

def say(function):
    text = function("Hi")
    print(text)
    return

say(quite)
say(loud)


def divisor(x):
    def dividend(y):
        return y / x
    return dividend

hof1 = divisor(2)
hof2 = hof1(10)

print(hof2) #0.5