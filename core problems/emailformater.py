print("Email Formatter")

email = input("Enter your email address: ")

if "@" not in email:
    print(" Invalid email format! Please include '@' symbol.")
else:
    username, domain = email.split("@")

    print("\n Extraction Result:")
    print(f"Username: {username}")
    print(f"Domain: {domain}")

    if "." in domain:
        domain_name = domain.split(".")[0]
        print(f"Domain Name (short): {domain_name}")