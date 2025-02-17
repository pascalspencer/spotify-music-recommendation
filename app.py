import spotipy
from spotipy.oauth2 import SpotifyOAuth
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
import spotipy
from spotipy.oauth2 import SpotifyOAuth




# Define your app's credentials and scope
client_id = "your_client_id"
client_secret = "your_client_secret"
redirect_uri = "your_redirect_uri"
scope = "user-top-read user-read-recently-played user-library-read"

# Create an OAuth object
auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)

# Create a Spotify object
sp = spotipy.Spotify(auth_manager=auth_manager)


# Get the user's top tracks
top_tracks = sp.current_user_top_tracks(limit=10)

# Print the track names and artists
for track in top_tracks["items"]:
    name = track["name"]
    artist = track["artists"][0]["name"]
    print(name, "-", artist)


# Get the user's most recently played track
recent_tracks = sp.current_user_recently_played(limit=1)
recent_track = recent_tracks["items"][0]["track"]
recent_track_id = recent_track["id"]
recent_track_name = recent_track["name"]
recent_track_artist = recent_track["artists"][0]["name"]

# Generate recommendations based on the recent track and target a high danceability
rec_tracks = sp.recommendations(seed_tracks=[recent_track_id], target_danceability=0.8, limit=10)

# Print the recommended track names and artists
print(f"Based on your recent track: {recent_track_name} - {recent_track_artist}")
print("We recommend these songs:")
for track in rec_tracks["tracks"]:
    name = track["name"]
    artist = track["artists"][0]["name"]
    print(name, "-", artist)


