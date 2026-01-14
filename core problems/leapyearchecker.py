def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 ==0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def main():
    print(" Leap year checker. ")
    try:
        year = int(input("Enter a year: "))
        if is_leap_year(year):
            print(f"{year} is Leap year")
        else:
            print("Not leap year")
    except ValueError:
        print("Enter Valid number. ")
            
if __name__ == "__main__":
    main()