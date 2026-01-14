def wordcounter():
    text = str(input("Enter Some text: "))
    words = text.split()
    count = len(words)
    char_count = len(text.replace(" ",""))
    print(count)
    print("Number of characters without spaces", char_count)
wordcounter()
