import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

#Get client id and client secret from system environment variables.
client_id =  os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

#Load the spotipy library using the credentials.
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Demo playlist to test ranking songs by popularity.
playlist_link = "https://open.spotify.com/playlist/0k0iV1RWW1PPaid4iXDPL5"
playlist_id = playlist_link.split("/")[-1]

#Compile tracks into a list.
results = sp.playlist_tracks(playlist_id)
tracks = results['items']
while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

#Sort the tracks by popularity and print their respective name, artist, and popularity.
sorted_tracks = sorted(tracks, key=lambda track: track['track']['popularity'], reverse=True)
for track in sorted_tracks:
    song_name = track['track']['name']
    artist_name = track['track']['artists'][0]['name']
    popularity = track['track']['popularity']
    print(f"{song_name} by {artist_name} - Popularity: {popularity}")