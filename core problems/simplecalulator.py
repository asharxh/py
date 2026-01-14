def add(num1, num2):
    return num1+num2
def substract(num1, num2):
    return num1-num2
def multiply(num1, num2):
    return num1*num2
def divide(num1, num2):
    return num1/num2

def calucaltor():
    while True:
        print("Weclome to SimpleCalulator")
        print("1. Addition(+)")
        print("2. Substraction(-)")
        print("3. Multiplication(*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("Enter Your choice from (1-5): ")
        if choice == 5:
            print("Exiting..... Goodbye")
            break
        if choice in ["1", "2", "3", "4"]:
            try:
                num1=float(input("Enter your first number: "))
                num2=float(input("Enter Your Second Number: "))
                
                if choice == "1":
                    print(f"result: {num1}+{num2} = {add(num1, num2)}")
                elif choice == "2":
                    print(f"result : {num1} - {num2} = {substract(num1,num2)}")
                elif choice =="3":
                    print(f"result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice =="4":
                    print(f"result: {num1} / {num2} = {divide(num1, num2)}")
            except ValueError:
                print("Please Enter valid input")
                
            else:
                print("Select valid input from 1 to 5")
            
calucaltor()
