
print("Even/Odd Position Extractor")

data = input("Enter a list of items separated by commas: ")

items = [item.strip() for item in data.split(",")]

if not items or items == ['']:
    print("No items provided! Please enter at least one value.")
else:
    even_positions = items[::2]
    odd_positions = items[1::2]
    
    print("\n Extraction Results:")
    print(f"Even position elements: {even_positions}")
    print(f"Odd position elements:  {odd_positions}")

print("\nProgram finished.")