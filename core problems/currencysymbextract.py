def extract_currency_symbol():
    value = input("Enter a currency value: ")
    symbols = ['$', '€', '£', '¥', '₹']
    symbol_found = ""
    index = 0
    while index < len(symbols):
        current_symbol = symbols[index]
        if value.startswith(current_symbol):
            symbol_found = current_symbol
            break
        elif value.endswith(current_symbol):
            symbol_found = current_symbol
            break
        else:
            index = index + 1
    if symbol_found == "":
        print("No currency symbol detected")
    else:
        print("Currency symbol is:", symbol_found)

extract_currency_symbol()