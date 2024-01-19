import csv

class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length

def load_music_library_dataset(file_path='dataset.csv'):
    songs_dataset = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            songs_dataset.append(Song(row['title'], row['artist'], row['album'], row['genre'], row['length']))
    return songs_dataset
