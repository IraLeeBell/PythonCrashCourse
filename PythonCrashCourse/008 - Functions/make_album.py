def make_album(artist_name, album_title, number_of_songs=''):
	album = {'Artist Name': artist_name, 'Album Title': album_title, 'Number of Songs': number_of_songs}
	return album

album_1 = make_album('nirvana', 'unplugged')
print(album_1)

album_2 = make_album('guns and roses', 'use your illusion', 3)
print(album_2)

album_3 = make_album('beatles', 'abbey road')
print(album_3)