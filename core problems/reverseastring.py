
print("Reverse a String")

text = input("Enter a string: ")

reversed_text = text[::-1]

print("\n Results:")
print(f"Original String: {text}")
print(f"Reversed String: {reversed_text}")

if text.lower() == reversed_text.lower():
    print("This is a palindrome!")
else:
    print("This is NOT a palindrome.")

print("\n Program completed successfully.")