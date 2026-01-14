print("MOVIE RATING SYSTEM")

movie_ratings = {}

while True:
    print("\n--- MENU ---")
    print("1. Add a movie and rating")
    print("2. Update a movie rating")
    print("3. View all movies and ratings")
    print("4. Search for a movie")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        movie = input("Enter movie name: ").strip().title()
        rating = float(input("Enter rating (1–5): "))
        if 1 <= rating <= 5:
            movie_ratings[movie] = rating
            print(f"Added '{movie}' with rating {rating}/5.")
        else:
            print("Rating must be between 1 and 5.")

    elif choice == '2':
        movie = input("Enter movie name to update: ").strip().title()
        if movie in movie_ratings:
            new_rating = float(input("Enter new rating (1–5): "))
            if 1 <= new_rating <= 5:
                movie_ratings[movie] = new_rating
                print(f" Updated '{movie}' rating to {new_rating}/5.")
            else:
                print(" Invalid rating! Must be between 1 and 5.")
        else:
            print("Movie not found!")

    elif choice == '3':
        if movie_ratings:
            print("\n All Movies and Ratings:")
            for m, r in sorted(movie_ratings.items()):
                print(f"- {m}: {r}/5")
        else:
            print(" No movies in the list yet.")

    elif choice == '4':
        movie = input("Enter movie name to search: ").strip().title()
        if movie in movie_ratings:
            print(f"'{movie}' has a rating of {movie_ratings[movie]}/5.")
        else:
            print("Movie not found.")

    elif choice == '5':
        print("Exiting Movie Rating System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")