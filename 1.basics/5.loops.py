import time
# while
name1 = ""
while len(name1) == 0:
    name1 = input("enter name1 : ")

name2 = None
while not name2:
    name2 = input("enter name 2 : ")



# for
for i in range(10):
    print("hi",i)

for i in "jasmine":
    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print('happy new year')


#nested for
for row in range(4):
    for col in range(8):
        print("@",end = "")
    print("")


# loop control
# break : used to terminate the loop entirely
# continue : skips to the next iteration of the loop
# pass  : does nothing, acts as a placeholder
    
while True:
    name = input("enter your name : ")
    if name != "":
        break

phone_number = "123_456_7890"
for i in phone_number:
    if i == "_":
        continue
    print(i,end="")

for i in range(1,21):
    if i == 13:
        pass
    else: 
        print(i)