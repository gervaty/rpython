def get_file_size(file_path):
    try:
        with open(file_path, 'rb') as file:
            file.seek(0, 2)
            file_size = file.tell()
            return file_size
    except FileNotFoundError:
        return -1
# -----------------------------------------------------------------------------
print("summabytes - this programd calculates summa byres in file")

file_path = input("Print file name: ")

file_size = get_file_size(file_path)
if file_size != -1:
    print(f"Size of file {file_path} is {file_size} byte.")
else:
    print("Error: you typed incorrect file name!")