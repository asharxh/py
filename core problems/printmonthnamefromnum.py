month_number = int(input("Enter month number (1-12): "))
months = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}
if month_number in months:
    print("Month name:", months[month_number])
else:
    print("Invalid month number.")