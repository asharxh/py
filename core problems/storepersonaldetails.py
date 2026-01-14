def store_personal_details():
    profile = {}
    name = input("Enter your name: ")
    age_input = input("Enter your age: ")
    age = int(age_input)
    gender = input("Enter your gender: ")
    country = input("Enter your country: ")
    email = input("Enter your email: ")
    profile["Name"] = name
    profile["Age"] = age
    profile["Gender"] = gender
    profile["Country"] = country
    profile["Email"] = email
    print("Personal Profile Details:")
    for key in profile:
        print(key + ":", profile[key])

store_personal_details()