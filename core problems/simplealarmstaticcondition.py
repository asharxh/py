import datetime
import time

print("SIMPLE ALARM / REMINDER")

alarm_time = "07:00"

print(f"Alarm set for {alarm_time}. Waiting...")

while True:
    current_time = datetime.datetime.now().strftime("%H:%M")
    
    if current_time == alarm_time:
        print("Reminder: It's time to wake up or complete your task!")
        break
    time.sleep(10)

print("Alarm finished. Have a good day!")