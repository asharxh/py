def mask_password():
    password = input("Enter your password: ")
    masked = ""
    index = 0
    while index < len(password):
        masked = masked + "*"
        index = index + 1
    print("Masked password:", masked)

mask_password()