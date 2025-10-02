print('''   _____ _   _  ____ ______   ______ _____ ___ ___  _   _  
 | ____| \ | |/ ___|  _ \ \ / /  _ \_   _|_ _/ _ \| \ | | 
 |  _| |  \| | |   | |_) \ V /| |_) || |  | | | | |  \| | 
 | |___| |\  | |___|  _ < | | |  __/ | |  | | |_| | |\  | 
 |_____|_| \_|\____|_|_\_\|_|_|_|    |_| |___\___/|_| \_| 
                / \  | \ | |  _ \                         
               / _ \ |  \| | | | |                        
              / ___ \| |\  | |_| |                        
  ____  _____/_/__ \_\_|_\_|____/_ _____ ___ ___  _   _   
 |  _ \| ____/ ___|  _ \ \ / /  _ \_   _|_ _/ _ \| \ | |  
 | | | |  _|| |   | |_) \ V /| |_) || |  | | | | |  \| |  
 | |_| | |__| |___|  _ < | | |  __/ | |  | | |_| | |\  |  
 |____/|_____\____|_| \_\|_| |_|    |_| |___\___/|_| \_|  
                                                          ''')
alphabets= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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

yes_or_no="yes"
while yes_or_no=="yes":
    text=input("Type code to Encrypt or Decrypt :")
    shift=int(input("type the Shift Number :"))
    direction=input("Encrypt or Decrypt :").lower()
    if direction=="encrypt":
        encrypt(text,shift)
    elif direction=="decrypt":
        decrypt(text,shift)
    else:
        print("You Iddiot Type Correctly ")
    yes_or_no=input("Do You want to Continue ? Type Yes or No : ").lower()
    if yes_or_no=="no":
        print("Thank You")
        break;
    elif yes_or_no=="yes":
        continue;
    else:
        print("Have you Studied a Bit of English ?")

