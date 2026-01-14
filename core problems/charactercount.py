text = str(input("Enter a String: ")).lower()

count = 0
for char in text:
    count += 1
    
print(f"Total character: {count} ")

count_no_space = 0


for char in text:
    if char != " ":
        count_no_space += 1
        
print(f"characters without space : {count_no_space}")