alphabets= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
text=input("Type code to Encrypt or Decrypt :")
shift=int(input("type the Shift Number :"))
def encrypt(text,shift):
    cipher=""
    for char in text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position+shift)%52
            new_char=alphabets[new_position]
            cipher+=new_char
        else:
            cipher+=char
    print(f"The Encrypted Text is : {cipher}")
def decrypt(text,shift):
    decipher=""
    for char in text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=position-shift
            new_char=alphabets[new_position]
            decipher+=new_char
        else:
            decipher+=char
    print(f"The Decrypted Text is : {decipher}")
direction=input("Encrypt or Decrypt :").lower()
if direction=="encrypt":
    encrypt(text,shift)
elif direction=="decrypt":
    decrypt(text,shift)
else:
    print("You Iddiot Type Correctly ")
print("Thank You for your time ")
