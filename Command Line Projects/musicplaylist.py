import time
import random
import os

def load_playlist(filename="playlist.txt"):
    playlist = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    name, artist, duration, play_count = parts
                    playlist.append({
                        "name": name,
                        "artist": artist,
                        "duration": float(duration),
                        "play_count": int(play_count)
                    })
    return playlist

def save_playlist(playlist, filename="playlist.txt"):
    with open(filename, "w") as f:
        for song in playlist:
            f.write(f"{song['name']}|{song['artist']}|{song['duration']}|{song['play_count']}\n")

def display_song(song, index):
    print(f"{index+1}. {song['name']} by {song['artist']} - {song['duration']} min (Played {song['play_count']} times)")

def music_playlist_advanced():
    playlist = load_playlist()
    current_index = 0
    repeat_mode = False
    shuffle_mode = False

    while True:
        print("\n--- Advanced Music Playlist Organizer ---")
        print("1. Add Song")
        print("2. Remove Song")
        print("3. View Playlist")
        print("4. Search Song")
        print("5. Sort Playlist")
        print("6. Play Next Song")
        print("7. Play Previous Song")
        print("8. Shuffle On/Off")
        print("9. Repeat On/Off")
        print("10. Show Total Duration")
        print("11. Show Most Played Songs")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter song name: ")
            artist = input("Enter artist name: ")
            duration_input = input("Enter duration in minutes: ")
            if not duration_input.replace('.','',1).isdigit():
                print("Invalid duration.")
                continue
            duration = float(duration_input)
            playlist.append({"name": name, "artist": artist, "duration": duration, "play_count": 0})
            save_playlist(playlist)
            print(f"Added '{name}' by {artist} to playlist.")

        elif choice == "2":
            if len(playlist) == 0:
                print("Playlist is empty.")
                continue
            for idx, song in enumerate(playlist):
                display_song(song, idx)
            remove_input = input("Enter song number to remove: ")
            if not remove_input.isdigit() or int(remove_input) < 1 or int(remove_input) > len(playlist):
                print("Invalid input.")
                continue
            removed_song = playlist.pop(int(remove_input)-1)
            save_playlist(playlist)
            print(f"Removed '{removed_song['name']}' from playlist.")

        elif choice == "3":
            if len(playlist) == 0:
                print("Playlist is empty.")
            else:
                print("Current Playlist:")
                for idx, song in enumerate(playlist):
                    display_song(song, idx)

        elif choice == "4":
            keyword = input("Enter song name or artist to search: ").lower()
            found = False
            for idx, song in enumerate(playlist):
                if keyword in song['name'].lower() or keyword in song['artist'].lower():
                    display_song(song, idx)
                    found = True
            if not found:
                print("No matching songs found.")

        elif choice == "5":
            print("Sort by: 1. Name 2. Artist 3. Duration 4. Play Count")
            sort_choice = input("Enter your choice: ")
            if sort_choice == "1":
                playlist.sort(key=lambda x: x['name'].lower())
            elif sort_choice == "2":
                playlist.sort(key=lambda x: x['artist'].lower())
            elif sort_choice == "3":
                playlist.sort(key=lambda x: x['duration'])
            elif sort_choice == "4":
                playlist.sort(key=lambda x: x['play_count'], reverse=True)
            else:
                print("Invalid choice.")
                continue
            print("Playlist sorted successfully.")
            save_playlist(playlist)

        elif choice == "6":
            if len(playlist) == 0:
                print("Playlist is empty.")
                continue
            if shuffle_mode:
                current_index = random.randint(0, len(playlist)-1)
            song = playlist[current_index]
            print(f"Playing: {song['name']} by {song['artist']}")
            song['play_count'] += 1
            save_playlist(playlist)
            for i in range(1, int(song['duration']*60)+1, max(1,int(song['duration']*60/5))):
                time.sleep(0.2)
                print(f"Playing... {int(i/(song['duration']*60)*100)}%", end="\r")
            print(f"Finished playing: {song['name']}")
            if not repeat_mode:
                current_index = (current_index + 1) % len(playlist)

        elif choice == "7":
            if len(playlist) == 0:
                print("Playlist is empty.")
                continue
            current_index = (current_index - 1) % len(playlist)
            song = playlist[current_index]
            print(f"Playing previous song: {song['name']} by {song['artist']}")
            song['play_count'] += 1
            save_playlist(playlist)

        elif choice == "8":
            shuffle_mode = not shuffle_mode
            print(f"Shuffle mode is now {'ON' if shuffle_mode else 'OFF'}.")

        elif choice == "9":
            repeat_mode = not repeat_mode
            print(f"Repeat mode is now {'ON' if repeat_mode else 'OFF'}.")

        elif choice == "10":
            total_duration = sum(song['duration'] for song in playlist)
            print(f"Total playlist duration: {total_duration:.2f} minutes")

        elif choice == "11":
            if len(playlist) == 0:
                print("Playlist is empty.")
                continue
            sorted_playlist = sorted(playlist, key=lambda x: x['play_count'], reverse=True)
            print("Most Played Songs:")
            for song in sorted_playlist[:5]:
                print(f"{song['name']} by {song['artist']} - Played {song['play_count']} times")

        elif choice == "12":
            print("Exiting Music Playlist Organizer.")
            break

        else:
            print("Invalid choice. Please select again.")

music_playlist_advanced()