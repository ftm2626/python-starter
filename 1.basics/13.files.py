import os

file_path = "C:\\Users\\Jasmine\\Desktop\\test.txt"
copy_path = "C:\\Users\\Jasmine\\Desktop\\test_copy.txt"
move_path ="test.txt" # project path
text = "this is a text\nthis is the next line "

exists = os.path.exists(file_path)
is_file = os.path.isfile(file_path)
is_folder = os.path.isdir(file_path)

print(is_folder)

# read a file
with open(file_path) as test: # this method closes the file automatically
    print(test.read())

# write a file
with open(file_path,"a") as test: 
    test.write(text)


# "r" : read
# "w" : write
# "a" : append
    


# copy a file
# copyfile() : copies contents of a file
# copy() : copyfile() + permission mode + destination can be a directory
# copy2() : copy() + copies metadata (file's creation and modification times)
import shutil

shutil.copy(file_path,copy_path)


# move a file
os.replace(file_path,move_path)

# delete a file
os.remove(move_path)


# 03:06:00