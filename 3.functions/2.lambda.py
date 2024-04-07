# lambda functions : functions written in 1 line using lambda keyword, accepts any number of arguments, but only has one expression.
# (think of it as a shortcut)
# (useful if needed for a short period of time, throw-away)
# lambda parameters = expression

# def double(x):
#     return x * 2

double = lambda x:x*2
multiple = lambda x,y: x*y
print(multiple(2,10))

age_check = lambda age:True if age >=18 else False

print(age_check(9))