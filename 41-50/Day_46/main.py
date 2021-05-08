from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth 
from os import environ

CLIENT_ID = environ.get("CLIENT_ID_SPOTIFY")
CLIENT_SECRET = environ.get("CLIENT_SECRET_SPOTIFY")
REDIRECT_URL = "http://example.com"

date = input("Which year do you want to travel to? type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

soup = BeautifulSoup(response.text, "html.parser")

songs_names_span = soup.select(".chart-element__information__song")
songs_names = [song.getText() for song in songs_names_span]
song_uris = []

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URL,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    ))
user_id = sp.current_user()["id"]

for song in songs_names:
    result = sp.search(q=f"track:{song} year: {year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)

    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped'")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
