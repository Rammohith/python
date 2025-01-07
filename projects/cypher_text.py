alphabet= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']

direction = input("Type 'encode' to encrypt the text, 'decode' to decrypt the text: ")
text = input("Type the text which you want to encrypt or decrypt: ")
shift= int(input("Type by which number you want to encrypt or decrypt the text: "))

def encrypt(plain_text, shift_number):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_number
        new_letter = alphabet[new_position]
        cipher_text += new_letter
        
    print(f"The encrypted word is: {cipher_text}")
    

def decrypt(cipher_text, shift_number):
    plain_text=""
    for i in cipher_text:
        position=alphabet.index(i)
        new_position=position-shift_number
        new_letter=alphabet[new_position]
        plain_text+=new_letter
        
    print(f"The decrypted word is {plain_text}")
    
    
if direction=="encode":
    encrypt(plain_text=text, shift_number=shift)
        
elif direction=="decode":
    decrypt(cipher_text=text, shift_number=shift)
else:
    print("Wrong input typed")