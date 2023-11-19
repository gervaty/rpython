import os

def ifFileExists(fileName):
    if os.path.isfile(fileName):
        return True
    else:
        return False
    
def createFile(fileName):
    file = open(fileName, "w")
    file.close()
    return True

def printFileLinesCount(fileName):
    file = open(fileName, "r")
    lines = 0
    for line in file:
        lines += 1
    file.close()
    print("There are", lines, "line(s) in the file.")

def appendLineToFile(fileName, line):
    file = open(fileName, "a")
    file.write("\n" + line)
    file.close()

########################## Main Program ##########################

print("notes - this programm adds string to end of file")

fileName = input("Enter a file name: ")

if not ifFileExists(fileName):
    createFile(fileName)

printFileLinesCount(fileName)

string = ""
while string != "q":
    string = input("Enter a note or q to exit: ")
    if string == "q":
        break
    appendLineToFile(fileName, string)

a = input("Press <ENTER> to exit")