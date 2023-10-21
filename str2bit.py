def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

print("str2bit - this prigram translate str to ascii")
stri = str(input("Enter a string: "))

#text_to_bits(stri)
print("bits: " + text_to_bits(stri))k 