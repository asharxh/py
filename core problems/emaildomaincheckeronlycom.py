def email_domain_checker():
    email = input("Enter your email address: ")
    if "@" in email and email.endswith(".com"):
        print("Email is valid and has a .com domain.")
    else:
        print("Invalid email. Only .com domain is allowed.")

email_domain_checker()