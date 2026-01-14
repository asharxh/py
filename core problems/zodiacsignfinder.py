
print("Zodiac Sign Finder")
print("------------------------------")

day = int(input("Enter your birth day (1-31): "))
month = input("Enter your birth month (name or number): ").strip().lower()

months = {
    "january": 1, "february": 2, "march": 3, "april": 4,
    "may": 5, "june": 6, "july": 7, "august": 8,
    "september": 9, "october": 10, "november": 11, "december": 12
}

if month.isalpha():
    month = months.get(month, 0)
else:
    month = int(month)

zodiac = ""

if (month == 3 and day >= 21) or (month == 4 and day <= 19):
    zodiac = "Aries"
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    zodiac = "Taurus"
elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    zodiac = "Gemini"
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    zodiac = "Cancer"
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    zodiac = "Leo"
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    zodiac = "Virgo"
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    zodiac = "Libra"
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    zodiac = "Scorpio"
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    zodiac = "Sagittarius"
elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    zodiac = "Capricorn"
elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    zodiac = "Aquarius"
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    zodiac = "Pisces"
else:
    zodiac = "Invalid date entered!"

print(f"\nYour Zodiac Sign is: {zodiac}")
