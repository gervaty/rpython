def text_to_bits(text):
    bits = bin(int.from_bytes(text.encode(), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8)) + " "

print("str 2 bit - this program translates string to binary")
stri = str(input("Enter a string: "))

bbits = ""
for i in range(len(stri)):
    char_bits = text_to_bits(stri[i])
    bbits += char_bits
    print(f"Character '{stri[i]}' in bits: {char_bits}")
    
print(f"{stri} in bits: {bbits}")

pausee = input()
