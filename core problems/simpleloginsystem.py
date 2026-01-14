def loginsystem():
    
    login = {
        "user1" : "pass123",
        "ashar" : "12345",
        "dk" : "83uu"
    }
    
    attempt = 3
    
    while attempt > 0:
        username = input("Enter your user name: ")
        password = input("Enter ur password: ")
    
        if username in login and login[username] == password:
            print("login successfull! ")
        else:
            attempt -= 1
            print("incorrect username or password! ")
    if attempt == 0:
        print("Too many failed attempt. Access Denied")
loginsystem()