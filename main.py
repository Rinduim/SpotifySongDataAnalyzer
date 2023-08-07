import json
from datetime import datetime
from collections import Counter
def main():
    songs_time = []
    songs = []
    artists = []
    for i in range(100):
        try:
            f = open("res\endsong_" + str(i) + ".json", encoding="utf8")
        except:
            break
        string = f.read()
        y = json.loads(string)
        for entry in y:
            datetime_object = datetime.strptime(entry["ts"], '%Y-%m-%dT%H:%M:%SZ')
            if entry["master_metadata_track_name"] != None:
                songs_time.append((datetime_object, entry["master_metadata_track_name"], entry["master_metadata_album_artist_name"]))
                songs.append((entry["master_metadata_track_name"], entry["master_metadata_album_artist_name"]))
                artists.append((entry["master_metadata_album_artist_name"]))
    songs_time.sort(key=lambda a: a[0])
    dictionary = Counter(songs)
    dictionary_artists = Counter(artists)

    # OUTPUT STUFF
    print_top_songs(dictionary, 10)
    print_top_artists(dictionary_artists, 10)
    print_song_stream_amount(dictionary,"Get Lucky (feat. Pharrell Williams & Nile Rodgers) - Radio Edit","Daft Punk")
    print_latest_songs(songs_time, 5)
    print_oldest_songs(songs_time, 10)
    print_streams_by_artist(songs, "Dame")
    print_streams_by_artist(songs, "Hollywood Undead")
    print_streams_by_artist(songs, "Bastille")

def print_top_songs(dictionary, amount): 
    print("The top", amount, "songs you streamed most:")
    counter = 1
    for key,value in dictionary.most_common(amount):
        print (str(counter) + ".", key, value)
        counter += 1
    print()
    
def print_top_artists(dictionary, amount): 
    print("The top", amount, "artists you streamed most:")
    counter = 1
    for key,value in dictionary.most_common(amount):
        print (str(counter) + ".", key, value)
        counter += 1
    print()

def print_song_stream_amount(dictionary, song_name, song_artist):
    print("You have listened to", song_name, "by", song_artist, dictionary[(song_name, song_artist)], "times.")
    print()

def print_latest_songs(songs_time, amount):
    print("Your", amount, "latest songs.")
    for i in range(amount):
        print(songs_time[len(songs_time)-i-1])
    print()

def print_oldest_songs(songs_time, amount):
    print("Your", amount, "oldest songs.")
    for i in range(amount):
        print(songs_time[i])
    print()

def print_streams_by_artist(songs, artist):
    counter = 0
    for song in songs:
        if song[1] == artist:
            counter += 1
    
    print("You listened to ", artist, str(counter), "times.")
    print()

    

if __name__ == "__main__":
    main()