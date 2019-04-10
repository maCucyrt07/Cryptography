"""
cryptography.py
Author: <your name here>
Credit: Andrew

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
a = 7
while a == 7:
    message = str(input("Enter e to encrypt, d to decrypt, or q to quit:"))
    if message == "q":
        a = 6
        
    for p in message:
        if p == "e":
        elif p == "d":
        elif p == "q": 
            break
        else: 
            print ("Did not understand command, try again."
print ("Goodbye!")
    

for char in text:
    print (associations.find(char))
for char in key:
    print (associations.find(char))


        