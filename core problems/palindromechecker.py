
word = str(input("Enter ur txt: ")).lower()
    
lenght = 0

for char in word:
    lenght += 1
    
is_palindrome = True
for i in range(lenght//2):
    if word[i] != word[lenght -i - 1]:
        is_palindrome = False
        break
    
if is_palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")        