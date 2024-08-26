#1.import logo
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
       position= alphabet.index(letter)
       new_position=position+shift_amount
       new_letter=alphabet[new_position]
       cipher_text+=new_letter
    print(f"The encode text is {cipher_text}")
    
    #2.  Inside the 'encrypt' function ,shift each letter of the 'text' forword in the alphabet
    # by the shift amount and print encrypted text.
     
    #3.Call the encrypt function and pass in the user inputs.
    # You should be able to test the code and encrypt a message.

#encrypt(plain_text=text,shift_amount=shift) 
#1 create a function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text,shift_amount):
    plain_text=""
    for letter in cipher_text:
        position=alphabet.index(letter)
        new_position=position-shift_amount
        plain_text+=alphabet[new_position]
    print(f"The decode text is {plain_text}")
#decrypt(cipher_text=text,shift_amount=shift)
 #2.  Inside the 'encrypt' function ,shift each letter of the 'text' backword in the alphabet
 # by the shift amount and print encrypted text.
 
 
 #3.Check if the user wanted to encrypt or decrypt the messang by checkimg the 'direction' variable.
 #Then call the correct function based om that 'direction' variable.You should be able to the test
 #the code to encrypt AND decrypt a message.
    if direction=="encode":
        encrypt(plain_text=text,shift_amount=shift)
    elif direction=="decode":
        decrypt(cipher_text=text,shift_amount=shift)
        
#1.Combine the encript and decript() function into a single function called caesar()

def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction=="decode":
            shift_amount *=-1
    for char in start_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position +shift_amount
            end_text+=alphabet[new_position]
        else:
            end_text+=char
    print(f"The {direction}d text result: {end_text}")
       # for char in start_text:
#2. call the caeser() function,passing over the 'text','shift' and 'ditrection' values.
#caesar(start_text=text,shift_amount=shift,cipher_direction=direction)  
#2. What if the user enters a shift that is greater than the number of letter in the alphabet
#Try running the programming and entering a shift number of 45.
#Hints: Think about how you can use the modules(%).
should_continue=True
while should_continue:
    direction=input("Type 'encode' to encrypt,type 'decode' to decrypt:\n")
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    #1 create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    shift=shift % 26
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction) 
    result=input("Type 'yes' if you want to go again.Otherwise type 'no'.\n")
    if result=="no":
        should_continue=False
        print("Good Bye")