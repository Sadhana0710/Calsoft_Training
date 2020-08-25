""" file handling"""

file = open("new_file.txt","w+")

file.write("This is our new file!\n")

file.close()

file = open("new_file.txt","a+")
file.write("Add new line!")

file = open("new_file.txt","r")
print(file.read())
