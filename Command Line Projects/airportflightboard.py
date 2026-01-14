import os
import datetime

def load_flights(filename="flights.txt"):
    flights = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 5:
                    flight_number, airline, destination, time_str, status = parts
                    flights.append({
                        "flight_number": flight_number,
                        "airline": airline,
                        "destination": destination,
                        "time": time_str,
                        "status": status
                    })
    return flights

def save_flights(flights, filename="flights.txt"):
    with open(filename, "w") as f:
        for flight in flights:
            f.write(f"{flight['flight_number']}|{flight['airline']}|{flight['destination']}|{flight['time']}|{flight['status']}\n")

def display_flight(flight):
    print(f"{flight['flight_number']} | {flight['airline']} | {flight['destination']} | {flight['time']} | {flight['status']}")

def airport_flight_board():
    flights = load_flights()

    while True:
        print("\n--- Airport Flight Board ---")
        print("1. Add Flight")
        print("2. Remove Flight")
        print("3. View All Flights")
        print("4. Search Flight")
        print("5. Update Flight Status")
        print("6. Sort Flights")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            flight_number = input("Enter flight number: ")
            if any(f['flight_number'] == flight_number for f in flights):
                print("Flight number already exists.")
                continue
            airline = input("Enter airline: ")
            destination = input("Enter destination: ")
            time_input = input("Enter scheduled time (HH:MM): ")
            try:
                datetime.datetime.strptime(time_input, "%H:%M")
            except ValueError:
                print("Invalid time format.")
                continue
            status = "On Time"
            flights.append({
                "flight_number": flight_number,
                "airline": airline,
                "destination": destination,
                "time": time_input,
                "status": status
            })
            save_flights(flights)
            print(f"Flight {flight_number} added successfully.")

        elif choice == "2":
            flight_number = input("Enter flight number to remove: ")
            for flight in flights:
                if flight['flight_number'] == flight_number:
                    flights.remove(flight)
                    save_flights(flights)
                    print(f"Flight {flight_number} removed successfully.")
                    break
            else:
                print("Flight not found.")

        elif choice == "3":
            if len(flights) == 0:
                print("No flights scheduled.")
            else:
                print("Flight Board:")
                for flight in flights:
                    display_flight(flight)

        elif choice == "4":
            keyword = input("Enter flight number, airline, or destination to search: ").lower()
            found = False
            for flight in flights:
                if (keyword in flight['flight_number'].lower() or
                    keyword in flight['airline'].lower() or
                    keyword in flight['destination'].lower()):
                    display_flight(flight)
                    found = True
            if not found:
                print("No matching flights found.")

        elif choice == "5":
            flight_number = input("Enter flight number to update status: ")
            for flight in flights:
                if flight['flight_number'] == flight_number:
                    print("Update status options: 1. On Time 2. Delayed 3. Departed 4. Cancelled")
                    status_choice = input("Enter your choice: ")
                    status_map = {"1": "On Time", "2": "Delayed", "3": "Departed", "4": "Cancelled"}
                    if status_choice in status_map:
                        flight['status'] = status_map[status_choice]
                        save_flights(flights)
                        print(f"Flight {flight_number} status updated to {flight['status']}.")
                    else:
                        print("Invalid choice.")
                    break
            else:
                print("Flight not found.")

        elif choice == "6":
            print("Sort by: 1. Flight Number 2. Airline 3. Time")
            sort_choice = input("Enter choice: ")
            if sort_choice == "1":
                flights.sort(key=lambda x: x['flight_number'])
            elif sort_choice == "2":
                flights.sort(key=lambda x: x['airline'].lower())
            elif sort_choice == "3":
                flights.sort(key=lambda x: datetime.datetime.strptime(x['time'], "%H:%M"))
            else:
                print("Invalid choice.")
                continue
            save_flights(flights)
            print("Flights sorted successfully.")

        elif choice == "7":
            print("Exiting Airport Flight Board.")
            break

        else:
            print("Invalid choice. Please select again.")

airport_flight_board()