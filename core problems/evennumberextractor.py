def extract_even_number(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
        
    return evens

def main():
    print("Welcome to Even no. Extractor. ")
    try:
        user_input = input("Enter Number of List Seprated by space: ")
        numbers = [int(x) for x in user_input.split()]
        evens = extract_even_number(numbers)
        
        if evens:
            print(f"Even numbers: {evens}")
        else:
            print("No even numbers found. ")
            
    except ValueError:
        print(" Please enter only Numbers. ")
        
main()