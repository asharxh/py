list1 = []
list2 = []
n1 = int(input("Enter number of elements in first list: "))
for i in range(n1):
    item = input("Enter element: ")
    list1.append(item)

n2 = int(input("Enter number of elements in second list: "))
for i in range(n2):
    item = input("Enter element: ")
    list2.append(item)

common = []
for i in list1:
    for j in list2:
        if i == j and i not in common:
            common.append(i)

print("Common elements:", common)