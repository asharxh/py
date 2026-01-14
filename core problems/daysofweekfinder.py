day = int(input("Enter day (1-31): "))
month = int(input("Enter month 1-12: "))
year = int(input("Enter Year: "))

if month == 1:
    month = 13
    year -= 1
elif month == 2:
    month = 14
    year -= 1
    
q = day
m = month
k = year % 100
j = year // 100

h = (q + (13*(m+1)) // 5 + k + (k//4) + (j//4) + 5*j) % 7 

days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]

print("The day is:", days[h])