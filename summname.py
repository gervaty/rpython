print("summname - this programd calculates summa of ascii codes in your word.")

wordd = ""
summaa = 0

wordd = input("Enter a word: ")

for i in range(len(wordd)):
    summaa += ord(wordd[i])

print(summaa)