def find_max_min(numbers):
    
    maximum = numbers[0]
    minimum = numbers[0]
    
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
            
    return maximum, minimum
        
def main():
    print("Min Max Finder. ")
    
    try:
        user_input = input("Enter numbers seprated by spaces: ")
        numbers = [int(x) for x in user_input.split()]
        
        maximum, minimum = find_max_min(numbers)
        
        print(f"Maximum number: {maximum}. ")
        print(f"minimum number: {minimum}. ")
    except ValueError:
        print("Please enter only number. ")
        
        
main()