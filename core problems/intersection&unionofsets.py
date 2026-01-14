input_set1 = input("Enter ur set1 (Seprated by comma)")
input_set2 = input("Enter ur set2 (Seprated by comma)")

set1 = set(input_set1.replace(" ", "").split(","))
set2 = set(input_set2.replace(" ", "").split(","))

union = set1 | set2
intersection = set1 & set2

print("Union of the sets:", union)
print("Intersection of the sets:", intersection)
