def km_to_miles(km):
    return km * 0.621371
def miles_to_km(miles):
    return miles / 0.621371
def meters_to_feet(meter):
    return meter * 3.28084
def feet_to_meter(feet):
    return feet / 3.28084
def cm_to_inches(cm):
    return cm / 2.54
def inches_to_cm(inches):
    return inches * 2.54

def main():
    print(" Simple Unit Converter. ")
    print("Choose Conversion [1. for km to miles] [2. for miles to km] [3. for meter to feet] [4. for feet to meter] [5. for cm to inches] [6. for inches to cm]")
    
    choice = input("Enter your choice (1-6): ")
    
    try:
            value = float(input("Enter the value to convert: "))
            
            if choice == "1":
                print(f" {value} km = {km_to_miles(value):.2f} miles")
            elif choice == "2":    
                print(f" {value} miles = {miles_to_km(value):.2f} km")
            elif choice == "3":
                print(f" {value} meters = {meters_to_feet(value):.2f} feet")
            elif choice == "4":
                print(f" {value} feet = {feet_to_meter(value):.2f} meters")
            elif choice == "5":
                print(f" {value} cm = {cm_to_inches(value):.2f} inches")
            elif choice == "6":
                print(f" {value} inches = {inches_to_cm(value):.2f} cm")
            else:
                print("Invalid Choice. ")
    except ValueError:
            print("Please enter valid number. ")
        
main()
