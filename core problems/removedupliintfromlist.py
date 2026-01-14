numbers_input = input("Enter numbers separated by spaces: ")
numbers_str = numbers_input.split()

numbers = []
for num in numbers_str:
    numbers.append(int(num)) 

unique_numbers = []
for num in numbers:
    if num not in unique_numbers: 
        unique_numbers.append(num)

print("Original list:", numbers)
print("List after removing duplicates:", unique_numbers)