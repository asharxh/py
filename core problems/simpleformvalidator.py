
print("=== Simple Form Validator ===\n")

name = input("Enter your full name: ").strip()
email = input("Enter your email: ").strip()
age = input("Enter your age: ").strip()
phone = input("Enter your phone number: ").strip()

errors = []

if len(name) == 0:
    errors.append("Name cannot be empty.")
elif not all(ch.isalpha() or ch.isspace() for ch in name):
    errors.append("Name must contain only letters and spaces.")

if "@" not in email or "." not in email:
    errors.append("Invalid email format.")

if not age.isdigit():
    errors.append("Age must be a number.")
else:
    age_num = int(age)
    if age_num < 1 or age_num > 120:
        errors.append("Age must be between 1 and 120.")
if not phone.isdigit():
    errors.append("Phone number must contain only digits.")
elif len(phone) != 10:
    errors.append("Phone number must be exactly 10 digits long.")

print("\n=== Validation Results ===")

if len(errors) == 0:
    print("All fields are valid. Form submitted successfully!")
else:
    print("Form has the following errors:")
    for err in errors:
        print("-", err)

if len(errors) > 0:
    print("\nPlease correct the errors and try again.")