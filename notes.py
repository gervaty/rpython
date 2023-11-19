#print("notes - this programm adds string to end of file")
#
#file_path = input("Print file name: ")
#stringg = input("Print string (your note): ")
import os
print("notes - this programm adds string to end of file")

fileforopen = input("Enter a file name: ")

file = open(fileforopen), "r"

string = ""
lines = 0

for line in file:
    lines += 1

if lines > 1:
    print(f"There are {lines} lines in this file")
if lines < 2:
    print("There is 1 line in this file")

file.close()

file = open(fileforopen), "a"

while string != "q":
    string = input("Enter a note or q to exit: ")

    if string == "q":
        break

    file.write("\n" + string)

file.close()
