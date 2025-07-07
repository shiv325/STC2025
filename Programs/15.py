text = input("Enter Text to Encrpyt => ")
encryptedText = ""
for c in text :
    if c == "Z" :
        encryptedText += "A"
    else :
        encryptedText += chr(ord(c) + 1)
print(f"Encrypted Text => {encryptedText}")
text = input("Enter Text to decrpyt=> ")
decryptedText = ""
for c in text :
    if c == "A" :
        decryptedText += "Z"
    else :
        decryptedText += chr(ord(c) - 1)
print(f"Decrypted Text => {decryptedText}")