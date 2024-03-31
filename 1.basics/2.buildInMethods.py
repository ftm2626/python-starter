import math;


# ----------------------STRING----------------------
name = "jasMine"
digit_name = "235689" 

length = len(name)
find_index = name.find("a")
cap = name.capitalize()
is_uppercase = name.isupper()
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

# str.format()

animal="cow"
item="moon"
formated_str1="the {} jumped over the {}".format(animal,item)
formated_str2="the {1} jumped over the {0}".format(animal,item)
formated_str3="the {animal} jumped over the {item}".format(animal=animal,item=item)
formated_str4="the {:10} jumped over the ".format(animal) # adds space

# print(formated_str4)


# ------------------------NUMBERS-------------------
# import math;
pi = 3.14159
million = 1000000
round_num = round(pi)
ceil_num = math.ceil(pi)
floor_num = math.floor(pi)
abs_num = abs(pi)
power_num = pow(pi,3)
squire_num = math.sqrt(420)
max_num = max(1,2,3,4)
min_num = min(1,2,3,4)
fifty_to_hundred_evens = range(50,100+1,2) # range(start,end,step)
format_2_digits = "number is {:.2f}".format(pi) # 3.14
comma ="number is {:,}".format(million) #1,000,000
 
print(comma)



# --------------------GENERAL---------------------
# index optator: gives access to a sequence's of element (str, list, tuples)

full_Name = "jasmine hunt"
indexing_first_name = full_Name[:6]