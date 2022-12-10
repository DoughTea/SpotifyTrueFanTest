import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.util import prompt_for_user_token

client_id = "00eb5624c52547b49144df266642f49e"
client_secret = "a605e0ac322740fba35a52a7dabfd9c7"
redirect_uri = "http://andrewdoty.pythonanywhere.com/"

# Prompt the user to log in and grant access to your app
token = prompt_for_user_token(username, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

# Use the token to create a Spotify object that can make authenticated requests
sp = spotipy.Spotify(auth=token)

# Make an authenticated request to the Spotify API
results = sp.current_user_saved_tracks()
print(results)
