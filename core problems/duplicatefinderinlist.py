input_text = str(input("Enter ur text seprated by space ")).split()

seen = set()
duplicate = set()

for item in input_text:
    if item in seen:
        duplicate.add(item)
    else:
        seen.add(item)
        
if duplicate:
    print("Duplicate elements found: ".join(duplicate))
else:
    print("No duplicate found in the list.")