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
            b = input("Message:")
            c = input("Key:")
            t = ''
            while True:
                t += c
                if len(t) >= len(b):
                    break
            m = [associations.find(y) for y in b]
            n = [associations.find(z) for z in t]
            o = [m + n for m, n in zip(m, n)]
            j = ''.join(associations[v % len(associations)] for v in o)
            print(j)
        elif p == "d":
            b = input("Message:")
            c = input("Key:")
            t = ''
            while True:
                t += c
                if len(t) >= len(b):
                    break
            m = [associations.find(y) for y in b]
            n = [associations.find(z) for z in t]
            o = [m - n for m, n in zip(m, n)]
            j = ''.join(associations[v % len(associations)] for v in o)
            print(j)
        elif p == "q": 
            break
        else: 
            print ("Did not understand command, try again.")
            
print ("Goodbye!")
    


        