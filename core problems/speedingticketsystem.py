print("""
      ----------------------
      SPEEDING TICKET SYSTEM
      ----------------------
      """)

speed_limit = float(input("Enter the speed limit (km/h): "))
driver_speed = float(input("Enter the driver's speed (km/h): "))

if driver_speed <= speed_limit:
    print("No Ticket! You are within the speed limit.")
elif driver_speed <= speed_limit + 20:
    print("Minor Violation! You are over the limit.")
    print("Fine: 500")
else:
    print("Major Violation! You exceeded the limit by more than 20 km/h.")
    print("Fine: 2000")
    print("Possible license suspension!")

print("\n--- Summary ---")
print(f"Speed Limit: {speed_limit} km/h")
print(f"Your Speed: {driver_speed} km/h")
if driver_speed <= speed_limit:
    print("Result: No Fine.")
elif driver_speed <= speed_limit + 20:
    print("Result: Minor Fine 500.")
else:
    print("Result: Major Fine 2000 + possible suspension.")