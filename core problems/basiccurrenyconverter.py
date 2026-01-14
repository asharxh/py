dict = {
    "USD" : 1,
    "INR" : 90,
    "AED" : 3.67,
    "EUR" : 0.92,
    "YEN" : 0.0068
}

print("Available curreny: ")
for curreny in dict:
    print("-", curreny)

amount = float(input("Enter the amount to be converted : "))
source = input("Enter the source Curreny: ").upper()
target = input("Enter the target curreny: ").upper()

if source not in dict or target not in dict:
    print("Invalid curreny code Entered! Try agin! ")
else:
    usd_amount = amount / dict[source]
    converted_amount = usd_amount * dict[target]
    
    print(f" {amount:.2f} {source} = {converted_amount:.2f} {target}")
        
