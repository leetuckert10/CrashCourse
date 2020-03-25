# Exercise 8-7: Album
#   Define a function that takes three parameters: artist_name, album_title,
# and optionally, num_songs. The function should return a dictionary of the
# data.


def make_album(artist_name, album_title, num_songs=None):
    album = {
        'name': artist_name,
        'album': album_title,
        'num_songs': num_songs,
    }
    return album


artists = []
artists.append(make_album('scorpions', 'savage amusement'))
artists.append(make_album('black sabath', 'paranoid'))
artists.append(make_album('led zepplin', 'led zepplin i'))
artists.append(make_album('scorpions', 'savage amusement', 10))

for artist in artists:
    print(f"{artist}")
