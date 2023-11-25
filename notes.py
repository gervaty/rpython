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
    print("There are", lines, "note(s) in the file.")

def appendLineToFile(fileName, line):
    file = open(fileName, "a")
    file.write(line + "\n")
    file.close()

def read_file(fileName):
    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File {fileName} not found.")
    except Exception as e:
        print(f"Error: {e}")

########################## Main Program ##########################

print("----- notes ver 4 -----")

fileName = input("Enter a notes` file name: ")


if not ifFileExists(fileName):
    createFile(fileName)

printFileLinesCount(fileName)

openmode = input("Choose a mode [a] - add notes [r] - see notes [q] - quit: ")

string = ""

if openmode == "a":
    file = open(fileName, "a")

    while string != "q":
        string = input("Enter a note or q to exit: ")

        if string == "q":
            break

        appendLineToFile(fileName, string)

    file.close()
if openmode == "r":
    read_file(fileName)


a = input("Press <ENTER> to exit")