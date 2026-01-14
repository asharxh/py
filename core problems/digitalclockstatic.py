def digital_clock():
    hours_input = input("Enter hours (00-23): ")
    minutes_input = input("Enter minutes (00-59): ")
    seconds_input = input("Enter seconds (00-59): ")
    hours = int(hours_input)
    minutes = int(minutes_input)
    seconds = int(seconds_input)
    if hours < 0 or hours > 23:
        print("Invalid hours input.")
    elif minutes < 0 or minutes > 59:
        print("Invalid minutes input.")
    elif seconds < 0 or seconds > 59:
        print("Invalid seconds input.")
    else:
        hours_str = str(hours)
        minutes_str = str(minutes)
        seconds_str = str(seconds)
        if len(hours_str) == 1:
            hours_str = "0" + hours_str
        if len(minutes_str) == 1:
            minutes_str = "0" + minutes_str
        if len(seconds_str) == 1:
            seconds_str = "0" + seconds_str
        print("Digital Clock Time: " + hours_str + ":" + minutes_str + ":" + seconds_str)

digital_clock()