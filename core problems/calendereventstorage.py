print(" Calendar Event Storage \n")

events = {} 

while True:
    print("\nChoose an option:")
    print("1. Add Event")
    print("2. View Events")
    print("3. Delete Event")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ").strip()
        event = input("Enter event description: ").strip()
        if date in events:
            events[date].append(event)
        else:
            events[date] = [event]
        print(" Event added successfully!")

    elif choice == "2":
        date = input("Enter date to view events (YYYY-MM-DD): ").strip()
        if date in events:
            print(f"Events on {date}:")
            for i, e in enumerate(events[date], 1):
                print(f"{i}. {e}")
        else:
            print("No events found for this date.")

    elif choice == "3":
        date = input("Enter date to delete event (YYYY-MM-DD): ").strip()
        if date in events:
            print(f"Events on {date}:")
            for i, e in enumerate(events[date], 1):
                print(f"{i}. {e}")
            delete_index = input("Enter event number to delete (or 'all' to delete all): ").strip()
            if delete_index.lower() == "all":
                del events[date]
                print(" All events deleted for this date.")
            elif delete_index.isdigit() and 1 <= int(delete_index) <= len(events[date]):
                deleted_event = events[date].pop(int(delete_index) - 1)
                print(f" Deleted: {deleted_event}")
                if not events[date]:
                    del events[date]
            else:
                print("Invalid selection.")
        else:
            print("No events found for this date.")

    elif choice == "4":
        print("\n=== Saving and exiting... ===")
        with open("calendar_events.txt", "w") as f:
            for date, ev_list in events.items():
                for ev in ev_list:
                    f.write(f"{date}: {ev}\n")
        print(" All events saved to 'calendar_events.txt'")
        print(" Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
