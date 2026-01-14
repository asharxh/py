keys = []
values = []
n = int(input("Enter number of items: "))
for i in range(n):
    k = input("Enter key: ")
    keys.append(k)
for i in range(n):
    v = input("Enter value: ")
    values.append(v)

dictionary = {}
for i in range(n):
    dictionary[keys[i]] = values[i]

print("Created dictionary:", dictionary)