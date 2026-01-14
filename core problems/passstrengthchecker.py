import string


password = input("Enter ur password: ")
strenght = 0

if len(password) >= 8 :
    strenght += 1
if any(c.islower() for c in password):
    strenght += 1
if any (c.isdigit() for c in password):
    strenght += 1
if any(c in string.punctuation for c in password):
    strenght += 1
    
if strenght <= 1:
    print("Weakk Password Strenght :(")
elif strenght == 2 or strenght ==3:
    print("Medium Password Strenght :|")
else:
    print("Password Strenght is Strong :)")
        