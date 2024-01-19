"""
You are part of a team developing a new music streaming app called "MFun." Your task is to design the core functionality that manages the user's music library and playlist creation. Consider the following requirements:

Music library:
Needs to store a collection of songs and their associated metadata (title, artist, album, genre, length).
Must efficiently retrieve songs by various criteria (artist, album, genre, title).
Must prevent duplicate song entries.

Playlists:
Users can create unlimited playlists.
Each playlist can contain any number of songs, but a song cannot be added multiple times to the same playlist.
Songs can be added, removed, or reordered within playlists.
The app should display songs in the order they were added to the playlist.

Which data structure model(s) would you choose to implement the music library and playlist features? Explain your choices, considering the characteristics of each data structure and the specific requirements of the application.

Data structures to consider:
       Tuples, Sets, Lists, Dictionaries, Trees, Graphs, Stacks, Queues
"""
# Prototype code, you can follow different implementation process
class MusicLibrary:
    def __init__(self):
        self.songs = {}

    def add_song(self, song):
        key = (song.title, song.artist, song.album)
        if key not in self.songs:
            self.songs[key] = song

    def get_songs_by_artist(self, artist):
        return [song for song in self.songs.values() if song.artist == artist]

    def get_songs_by_album(self, album):
        return [song for song in self.songs.values() if song.album == album]

    def get_songs_by_genre(self, genre):
        return [song for song in self.songs.values() if song.genre == genre]

    def get_songs_by_title(self, title):
        return [song for song in self.songs.values() if song.title == title]

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def reorder_songs(self, new_order):
        self.songs = list(set(new_order))

    def display_playlist(self):
        print(f"Playlist: {self.name}")
        for i, song in enumerate(self.songs, 1):
            print(f"{i}. {song.title} - {song.artist}")

        print(f"\nSongs by {self.name}:")
        for song in self.songs:
            print(f"{song.title} - {song.album}")




# Main Requirement:
# Create song example
# Create a music library
# Add songs to the music library
# Get songs by artist
# Create playlists
# Add songs to playlists
# Display playlists
# Searching for songs by artist

# Sample Output:
'''Playlist: My Playlist 1
1. Song 1 - Artist 1
2. Song 2 - Artist 2

Songs by Artist 1:
Song 1 - Album 1'''
