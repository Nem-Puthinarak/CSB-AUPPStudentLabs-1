from streaming_dataset import load_music_library_dataset , Song
from musicstreamingapp import MusicLibrary, Playlist 

def main():
    music_library = MusicLibrary()
    playlists = []

    # Initialize music library with a realistic dataset
    for song in load_music_library_dataset():
        music_library.add_song(song)

    while True:
        print("\nOptions:")
        print("1. Add Song to Music Library")
        print("2. Create Playlist")
        print("3. Add Song to Playlist")
        print("4. Remove Song from Playlist")
        print("5. Reorder Songs in Playlist")
        print("6. Display Playlists")
        print("7. Search Songs by Artist")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            title = input("Enter song title: ")
            artist = input("Enter artist: ")
            album = input("Enter album: ")
            genre = input("Enter genre: ")
            length = input("Enter length: ")
            song = Song(title, artist, album, genre, length)
            music_library.add_song(song)
            print(f"Song '{title}' added to the music library.")

        elif choice == "2":
            playlist_name = input("Enter playlist name: ")
            playlists.append(Playlist(playlist_name))
            print(f"Playlist '{playlist_name}' created!")

        elif choice == "3":
            playlist_name = input("Enter playlist name: ")
            title = input("Enter song title to add: ")
            matching_songs = music_library.get_songs_by_title(title)

            if matching_songs:
                selected_song = matching_songs[0]
                for playlist in playlists:
                    if playlist.name == playlist_name:
                        playlist.add_song(selected_song)
                        print(f"Song '{selected_song.title}' added to '{playlist.name}'.")
            else:
                print(f"Song '{title}' not found in the library. Add it to the library first.")

        elif choice == "4":
            playlist_name = input("Enter playlist name: ")
            title = input("Enter song title to remove: ")
            matching_songs = music_library.get_songs_by_title(title)

            if matching_songs:
                selected_song = matching_songs[0]
                for playlist in playlists:
                    if playlist.name == playlist_name:
                        playlist.remove_song(selected_song)
                        print(f"Song '{selected_song.title}' removed from '{playlist.name}'.")
            else:
                print(f"Song '{title}' not found in the playlist.")

        elif choice == "5":
            playlist_name = input("Enter playlist name: ")
            new_order = []
            while True:
                title = input("Enter song title to add to the new order (press Enter to finish): ")
                if not title:
                    break
                matching_songs = music_library.get_songs_by_title(title)
                if matching_songs:
                    new_order.append(matching_songs[0])
                else:
                    print(f"Song '{title}' not found in the library.")
            for playlist in playlists:
                if playlist.name == playlist_name:
                    playlist.reorder_songs(new_order)
                    print(f"Songs reordered in '{playlist.name}'.")

        elif choice == "6":
            for playlist in playlists:
                playlist.display_playlist()

        elif choice == "7":
            artist_name = input("Enter artist name to search: ")
            matching_songs = music_library.get_songs_by_artist(artist_name)
            if matching_songs:
                print(f"Songs by {artist_name}:")
                for song in matching_songs:
                    print(f"{song.title} - {song.album} - {song.genre} - {song.length}")
            else:
                print(f"No songs found by {artist_name}.")

        elif choice == "8":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
