import os
import random

def load_weather(filename="weather.txt"):
    weather_data = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    city, temp, humidity, condition = parts
                    weather_data.append({
                        "city": city,
                        "temperature": float(temp),
                        "humidity": int(humidity),
                        "condition": condition
                    })
    return weather_data

def save_weather(weather_data, filename="weather.txt"):
    with open(filename, "w") as f:
        for w in weather_data:
            f.write(f"{w['city']}|{w['temperature']}|{w['humidity']}|{w['condition']}\n")

def display_city_weather(w):
    print(f"{w['city']} | Temp: {w['temperature']}°C | Humidity: {w['humidity']}% | Condition: {w['condition']}")

def weather_report_system():
    weather_data = load_weather()
    conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Windy", "Snowy"]

    while True:
        print("\n--- Weather Report System ---")
        print("1. Add City")
        print("2. Remove City")
        print("3. View All Cities")
        print("4. Search City")
        print("5. Update Weather")
        print("6. Sort Cities")
        print("7. Simulate Dynamic Updates")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter city name: ")
            if any(w['city'].lower() == city.lower() for w in weather_data):
                print("City already exists.")
                continue
            temp_input = input("Enter temperature (°C): ")
            humidity_input = input("Enter humidity (%): ")
            condition = input("Enter condition: ")
            if not temp_input.replace('.','',1).isdigit() or not humidity_input.isdigit():
                print("Invalid temperature or humidity.")
                continue
            weather_data.append({
                "city": city,
                "temperature": float(temp_input),
                "humidity": int(humidity_input),
                "condition": condition
            })
            save_weather(weather_data)
            print(f"City '{city}' added successfully.")

        elif choice == "2":
            city = input("Enter city name to remove: ")
            for w in weather_data:
                if w['city'].lower() == city.lower():
                    weather_data.remove(w)
                    save_weather(weather_data)
                    print(f"City '{city}' removed successfully.")
                    break
            else:
                print("City not found.")

        elif choice == "3":
            if len(weather_data) == 0:
                print("No cities available.")
            else:
                print("Weather Reports:")
                for w in weather_data:
                    display_city_weather(w)

        elif choice == "4":
            city = input("Enter city name to search: ").lower()
            found = False
            for w in weather_data:
                if city == w['city'].lower():
                    display_city_weather(w)
                    found = True
            if not found:
                print("City not found.")

        elif choice == "5":
            city = input("Enter city name to update: ").lower()
            for w in weather_data:
                if city == w['city'].lower():
                    temp_input = input(f"Enter new temperature (current: {w['temperature']}°C): ")
                    humidity_input = input(f"Enter new humidity (current: {w['humidity']}%): ")
                    condition = input(f"Enter new condition (current: {w['condition']}): ")
                    if temp_input:
                        if not temp_input.replace('.','',1).isdigit():
                            print("Invalid temperature.")
                            break
                        w['temperature'] = float(temp_input)
                    if humidity_input:
                        if not humidity_input.isdigit():
                            print("Invalid humidity.")
                            break
                        w['humidity'] = int(humidity_input)
                    if condition:
                        w['condition'] = condition
                    save_weather(weather_data)
                    print(f"City '{w['city']}' updated successfully.")
                    break
            else:
                print("City not found.")

        elif choice == "6":
            print("Sort by: 1. City 2. Temperature 3. Humidity")
            sort_choice = input("Enter choice: ")
            if sort_choice == "1":
                weather_data.sort(key=lambda x: x['city'].lower())
            elif sort_choice == "2":
                weather_data.sort(key=lambda x: x['temperature'])
            elif sort_choice == "3":
                weather_data.sort(key=lambda x: x['humidity'])
            else:
                print("Invalid choice.")
                continue
            save_weather(weather_data)
            print("Cities sorted successfully.")

        elif choice == "7":
            print("Simulating dynamic updates...")
            for w in weather_data:
                w['temperature'] += random.randint(-2, 3)
                w['humidity'] += random.randint(-5, 5)
                w['humidity'] = max(0, min(100, w['humidity']))
                w['condition'] = random.choice(conditions)
            save_weather(weather_data)
            print("Weather updated dynamically.")
            for w in weather_data:
                display_city_weather(w)

        elif choice == "8":
            print("Exiting Weather Report System.")
            break

        else:
            print("Invalid choice. Please select again.")

weather_report_system()