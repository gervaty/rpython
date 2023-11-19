import random
print("pwdgen 1.0 - universal password generator.")

#symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
symbols = "01"
while True:
    password = ""
    numStr = input("Type a number from 1 to 1024 or 0 to exit: ")

    if not numStr.isnumeric(): continue

    num = int(numStr)

    if num == 0: break

    for i in range(0, num):
        password += symbols[random.randint(0, len(symbols) - 1)]

    print(password)

input("Press <ENTER> to close this windows.")