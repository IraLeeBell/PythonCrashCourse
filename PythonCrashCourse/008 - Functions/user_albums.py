def make_album(artist_name, album_title, number_of_songs=''):
	album = {'Artist Name': artist_name, 'Album Title': album_title, 'Number of Songs': number_of_songs}
	return album

while True:
	print("\nThis will build an album dictionary.")
	print("\nPress 'q' to quit at any point.")
	artist = input("\nPlease enter an artist or band name. ")
	if artist == 'q':
		break
	album = input("\nPlease enter an album name. ")
	if album == 'q':
		break
	songs = input("\nplease enter the number of songs. ")
	if songs == 'q':
		break

	band_dictionary = make_album(artist, album, songs)
	print(band_dictionary)

