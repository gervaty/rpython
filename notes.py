#print("notes - this programm adds string to end of file")
#
#file_path = input("Print file name: ")
#stringg = input("Print string (your note): ")

file = open(input("Enter a file name: "), "a")

string = ""

while string != "q":
    string = input("Enter a note or q to exit: ")

    if string == "q":
        break

    file.write("\n" + string)

file.close()
