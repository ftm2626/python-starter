import math;


# ----------------------STRING----------------------
name = "jasMine"
digit_name = "235689" 

length = len(name)
find_index = name.find("a")
cap = name.capitalize()
uppercase =name.upper()
lowercase = name.lower()
is_digit = digit_name.isdigit() # True
is_alphabet = digit_name.isalpha() # False
count_how_many_chars = name.count("e") #1
jasmine_with_u = name.replace("e","u")
display_three_times = name * 3

# slicing : create a substring by extracting elements from another string
#       indexing[] : [start:stop:step]
full_name = "jasmine hunt"
second_letter = full_name[1]
first_name = full_name[0:7] # or full_name[:7]
weird_name = full_name[::2]
reverse_name = full_name[::-1]
#       slice()
website = "http://google.com"
website_name_index = slice(7,-4) #second params is nagative index that counts from right
website_name = website[website_name_index]




# ------------------------NUMBERS-------------------
# import math;
pi = 3.14
round_num = round(pi)
ceil_num = math.ceil(pi)
floor_num = math.floor(pi)
abs_num = abs(pi)
power_num = pow(pi,3)
squire_num = math.sqrt(420)
max_num = max(1,2,3,4)
min_num = min(1,2,3,4)
fifty_to_hundred_evens = range(50,100+1,2) # range(start,end,step)


print(website_name)