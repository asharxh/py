set1 = set()
set2 = set()
n1 = int(input("Enter number of elements in first set: "))
for i in range(n1):
    item = input("Enter element: ")
    set1.add(item)

n2 = int(input("Enter number of elements in second set: "))
for i in range(n2):
    item = input("Enter element: ")
    set2.add(item)

disjoint = True
for i in set1:
    if i in set2:
        disjoint = False
        break

if disjoint:
    print("The sets are disjoint.")
else:
    print("The sets are not disjoint.")
