# sort function: used with iterables not lists
food = ("pizza","burger","hotdog","pudding","pasta")

sorted_list = sorted(food)
reversed_sorted_list = sorted(food,reverse=True)

for i in sorted_list:
    print(i)


student = (("fatemeh","A",26),
           ("zahra","C",27),
           ("mohsen","A",25),
           ("ali","F",28),
           ("reza","B",30),)

grade = lambda grades:grades[1]

sorted_students = sorted(student,key=grade)

for i in sorted_students:
    print(i)