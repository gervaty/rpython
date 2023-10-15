import random
print("This is the program that generating super password.")
print("Prepearing values...")

symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
i = 0
while True:
    password = ""
    num = int(input("Type a number or 0 to exit: "))

    if num == "":
        print("You can't type the empty number!")
    if num > 1024:
        print("You can't type the number > 1024!")
    if num == 0: break
    for i in range(1, num):
        index = random.randint(0, len(symbols) - 1)
        password = password + symbols[index]
    print(password)

paus = str(input("Press <ENTER> to close this windows."))