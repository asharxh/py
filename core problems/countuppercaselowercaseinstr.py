text = input("Enter text to count Upper and Lower Case text by using space: ")

upper_count = 0
lower_count = 0

for upper in text:
    if text.isupper():
        upper_count += 1
    
    elif text.lower():
        lower_count += 1
print(f"Total upper count is {upper_count}")
print(f"Total lower count is {lower_count}")
    