def find_list_length():
    list_input = input("Enter list elements separated by spaces: ")
    items = list_input.split()
    count = 0
    index = 0
    while True:
        if index < len(items):
            count = count + 1
            index = index + 1
        else:
            break
    print("Number of elements in the list:", count)

find_list_length()