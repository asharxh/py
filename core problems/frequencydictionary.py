print("=== Frequency Dictionary ===\n")

words = input("Enter a sentence or a list of words: ").lower().split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("\nWord Frequency:")
for word, count in freq.items():
    print(f"{word}: {count}")

most_common = max(freq, key=freq.get)
print(f"\nMost frequent word: '{most_common}' ({freq[most_common]} times)")