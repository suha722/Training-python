from datetime import datetime


def convert_sec_to_min_and_sec(duration):
    """
    returns:the duration of song in minutes and second
    param :duration(int):the duration of song in seconds
    return min(tuple):duration after converted to second and minutes
    """
    duration_min_sec = (int(duration / 60), duration % 60)
    return duration_min_sec


def view_playlist(playlist):
    """
    returns:this function view the playlist
    :param playlist:(list_of_dictionary):list of dictionary have playlist
    :return: no return type print the playlist in prtty shap
    """
    print("___________Playlist_______________\n")
    for song in range(len(playlist)):
        playlistview = str(playlist[song])
        print(song + 1, end="")
        line = playlistview.replace('{', '_').replace('}', "").replace("'", "").replace(",", " _ ")
        print(line)


def search_in_playlist(playlist, word_search):
    """
    returns:this function search a word into the playlist
    :param playlist: list of dictionary have a playlist
    :param word_search: the user enterd to search
    :return: this call function view to return a list of playlist if found the word in it if not return empity
    playlist
    """
    searching_list = []
    for song in range(len(playlist)):
        if word_search in playlist[song].values():
            searching_list.append(playlist[song])

    else:
        print("Sorry we not found anything!")
    # pass the searching list to function view-playlist to show the playlist in pretty way
    return view_playlist(searching_list)


def filter_song(playlist, year, genre):
    """
    returns:this function prints the playlist of the same genre and year for you want
    param :playlist (list_of_dictionary):
    param year: the year of song you want
    param genre:the genre of song you want
    return: no return it is print the list of the song that has same type and list has the same year
    """
    filter_same_genre = []
    filter_same_year = []
    for song in range(len(playlist)):
        if playlist[song]["genre"] == genre:
            filter_same_genre.append(playlist[song])
        if playlist[song]["year"] == year:
            filter_same_year.append(playlist[song])
    print("The details in song in genre", genre, "is\n"
                                                 "__________________________________________\n")
    # for song_genre in filter_same_genre:
    print(view_playlist(filter_same_genre))
    print("___________________________________________________")
    print("The details in song in year:", year, "is\n")
    # for song_year in filter_same_year:
    print(view_playlist(filter_same_year))


def analyise_song_artist(playlist, artist):
    """
    returns:this function return the average of all song in the one artist you want and the sum of song
     and the totale of duration of all song
    :param playlist: the playlist of all song
    :param artist: the name of artist you want to find average for him
    :return :print the average of duration the all song for the one artist you want the , input_number of song and
    duration of all song in second
    """
    number_of_song = 0
    sum_of_duration = 0
    count_word = 0
    most_common_word = ''
    dic_of_most_common = {}
    oldest_song = playlist[0]["year"]
    new_song = playlist[0]["year"]
    for song in range(len(playlist)):
        if playlist[song]["artist"] == artist:
            number_of_song += 1
            sum_of_duration += playlist[song]["duration"]
        # find the common artist in all playlist
        for word in playlist[song]["artist"].split():
            if word in dic_of_most_common:
                dic_of_most_common[word] += 1
                if dic_of_most_common[word] > count_word:
                    count_word = dic_of_most_common[word]
                    most_common_word = word
            else:
                dic_of_most_common[word] = 1
        # find the oldest year and newest song
        if playlist[song]["year"] > playlist[0]["year"]:
            new_song = playlist[song]
        else:
            oldest_song = playlist[song]

    print("Total input_number of songs for ", artist, number_of_song, " songs")
    print("Total playlist length (seconds) for ", artist, sum_of_duration, "sec")
    average = sum_of_duration / number_of_song
    print("Average song length (seconds): ", artist, average, " sec")
    print("Oldest song: ", "Song Title: ", oldest_song["title"], "_Artist name: ", oldest_song["artist"],
          "_Album Name: ", oldest_song["genre"], " _year :", oldest_song["year"])
    print("Newest song:", "Song Title: ", new_song["title"], "_Artist name: ", new_song["artist"],
          "_Album Name: ", new_song["genre"], " _year :", new_song["year"])
    print("most common artist:", most_common_word, count_word)


def main_option(playlist):
    print("Welcome to the Music Playlist Analyzer!\n")
    print("1. Load Playlist \n"
          "2. View Playlist \n"
          "3. Search Playlist \n"
          "4. Analyze Playlist \n"
          "5. Convert second to minutes and second\n"
          "6. Filter the song built in year and genre\n"

          "7. Exit\n")
    newplaylist = {}
    while True:
        option = input("Enter your option: ")
        try:
            option = int(option)
            if option == 1:
                while True:
                    title = input("Enter the title of song").title()
                    if title.isalpha():
                        newplaylist["title"] = title
                        break
                    else:
                        print("the title must be string")

                while True:
                    artist = input("Enter the artist name ").title()
                    if artist.isalpha():
                        newplaylist["artist"] = artist
                        break
                    else:
                        print("the artist name must be string")
                while True:
                    genre = input("Enter the genre of song").title()
                    if genre.isalpha():
                        newplaylist["genre"] = genre
                        break
                    else:
                        print("the genre must be string")
                while True:
                    year = input("Enter the year of song")
                    if year.isdigit():
                        year = int(year)
                        date_today = datetime.today()
                        current_year = date_today.year
                        if year > 1000 and year <= current_year:
                            newplaylist["year"] = year
                            break
                        else:
                            print("the year must have four digit")
                    else:
                        print("the year must be input_number")

                while True:
                    duration = input("Enter the duration of song")

                    if duration.isdigit():
                        newplaylist["duration"] = duration
                        break
                    else:
                        print("the duration must be input_number")
                playlist.append(newplaylist)
                print("The playlist loaded successfully", view_playlist(playlist))
            if option == 2:
                view_playlist(playlist)
            if option == 3:
                word = input("Enter search term: ")
                print(search_in_playlist(playlist, word.title()))
            if option == 4:
                print("_____________________Analyse playlist__________________")
                artist = input("Enter the name of artist you want to analyse your songs and find the avarage ")
                analyise_song_artist(playlist, artist)
            if option == 5:
                for length_list in range(len(playlist)):
                    minutes, second = convert_sec_to_min_and_sec(playlist[length_list]["duration"])
                    print("The duration of song for", playlist[length_list]["title"], ": ", minutes, "m :", second, "s")
            if option == 6:
                while True:
                    genre = input("Enter the genre of song").title()
                    if genre.isalpha():
                        newplaylist["genre"] = genre
                        break
                    else:
                        print("the genre must be string")
                while True:
                    year = input("Enter the year of song")
                    if year.isdigit():
                        year = int(year)
                        date_today = datetime.today()
                        current_year = date_today.year
                        if year > 1000 and year <= current_year:
                            newplaylist["year"] = year
                            break
                        else:
                            print("the year must have four digit and  less than current year")
                    else:
                        print("the year must be input_number")
                filter_song(playlist, year, genre)
            if option == 7:
                print("Good bye!")
                break

        except ValueError:
            print("please enter option from the option view !")


Playlist = [{"title": "Bohemian Rhapsody", "artist": "Queen", "genre": "Rock", "year": 1975, "duration": 355},
            {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "genre": "Rock", "year": 1971, "duration": 482},
            {"title": "Hotel California", "artist": "The Eagles", "genre": "Rock", "year": 1977, "duration": 390},
            {"title": "Back in Black", "artist": "AC/DC", "genre": "Rock", "year": 1980, "duration": 255},
            {"title": "The Chain", "artist": "Fleetwood Mac", "genre": "Rock", "year": 1977, "duration": 288},
            {"title": "Highway to Hell", "artist": "AC/DC", "genre": "Rock", "year": 1979, "duration": 208},
            {"title": "Don't Stop Believin'", "artist": "Journey", "genre": "Rock", "year": 1981, "duration": 249},
            {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "genre": "Grunge", "year": 1991, "duration": 301},
            {"title": "Enter Sandman", "artist": "Metallica", "genre": "Metal", "year": 1991, "duration": 332},
            {"title": "November Rain", "artist": "Guns N' Roses", "genre": "Rock", "year": 1991, "duration": 537}]

main_option(Playlist)
