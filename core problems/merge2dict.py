dict1 = {}
dict2 = {}
n1 = int(input("Enter number of items for first dictionary: "))
for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

n2 = int(input("Enter number of items for second dictionary: "))
for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

merged_dict = {}
for k in dict1:
    merged_dict[k] = dict1[k]
for k in dict2:
    merged_dict[k] = dict2[k]

print("Merged dictionary:", merged_dict)