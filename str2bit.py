def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

print("str 2 bit - this programd translate str to ascii")
stri = str(input("Enter a string: "))

bbits = ""
for i in range(len(stri)):
    char_bits = text_to_bits(stri[i])
    bbits += char_bits
    print(f"Character '{stri[i]}' in bits: {char_bits}")
print(f"{stri} in bits: {bbits}")
