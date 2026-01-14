print("=== Simple Resume Builder ===\n")

name = input("Enter your full name: ")
email = input("Enter your email address: ")
phone = input("Enter your phone number: ")
address = input("Enter your address: ")

education = input("Enter your Education details: ")
skills = input("Enter your skills (comma seprated): ")
experience = input("Enter your work experience: ")
projects = input("Enter your projeccts (comma seprated): ")
hobbies = input("Enter your hobbies/interests: ")

resume = f"""
=============================================
            SIMPLE RESUME
=============================================

Name : {name}
Email : {email}
Phone : {phone}
Address : {address}

---------------------------------------------
Education:
{education}

---------------------------------------------
Skills:
{skills}

---------------------------------------------
Experience:
{experience}

---------------------------------------------
Projects:
{projects}

---------------------------------------------
Hobbies/Interests:
{hobbies}

=============================================
"""

print("\n" + resume)

save = input("Would you like to save this resume (Yes/No): ").lower()

if save == "yes":
    with open ("resume.txt", "w") as file:
        file.write(resume)
    print("\n Resume saved as 'resume.txt' ")
else:
    print("\nResume not Saved. ")
