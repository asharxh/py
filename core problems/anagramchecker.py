print("Anagram Checker\n")

while True:
    word1 = input("Enter the first word or phrase: ").lower()
    word2 = input("Enter the second word or phrase: ").lower()


    clean1 = "".join(ch for ch in word1 if ch.isalnum())
    clean2 = "".join(ch for ch in word2 if ch.isalnum())

    if sorted(clean1) == sorted(clean2):
        print("these are anagrams!\n")
    else:
        print(" Not anagrams.\n")

    again = input("Check another pair? (yes/no): ").lower()
    if again != "yes":
        print(" Goodbye!")
        break
