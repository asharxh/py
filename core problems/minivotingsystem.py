print("===Mini Voting System ===\n")

candidates = ["Ashar", "Bob", "Dk"]

votes = {candidate: 0 for candidate in candidates}

print("Candidates:")
for candidate in candidates:
    print("-", candidate)
print("\nType 'stop' to end voting.\n")

while True:
    choice = input("Enter your vote: ").title().strip()

    if choice.lower() == "stop":
        break

    if choice in votes:
        votes[choice] += 1
        print(f" Vote recorded for {choice}!")
    else:
        print(" Invalid candidate name. Please vote correctly.")

print("\n=== Voting Results ===")
for candidate, count in votes.items():
    print(f"{candidate}: {count} votes")

max_votes = max(votes.values())
winners = [name for name, count in votes.items() if count == max_votes]

if len(winners) == 1:
    print(f"\n Winner: {winners[0]} with {max_votes} votes!")
else:
    print(f"\n It's a tie between: {', '.join(winners)} ({max_votes} votes each)")
