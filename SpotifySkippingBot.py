import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth

# Setup Spotipy with your Spotify API credentials
CLIENT_ID = 'YOUR_CLIENT_ID'  # Replace with your Spotify Client ID
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'  # Replace with your Spotify Client Secret
REDIRECT_URI = 'http://localhost:8888/callback'  # Redirect URI

# Initialize Spotipy
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope='user-modify-playback-state user-read-playback-state'))

def skip_song_until_input():
    print("Skipping songs... Write an input to stop.")
    try:
        while True:
            current_playback = sp.current_playback()  # Get the current playback state

            if current_playback and current_playback['is_playing']:
                if current_playback['progress_ms'] >= 60000:  # Check if the song has been playing for at least 60 seconds
                    sp.next_track()  # Skip to the next track
                    print("Skipped to the next song.")

            time.sleep(1)  # Wait for a short time before checking again

            if input():  # Check for user input to stop the bot
                print("Skipping bot stopped by user.")
                break
    except KeyboardInterrupt:  # Handle Ctrl + C
        print("Skipping Bot stopped by user.")

if __name__ == "__main__":
    skip_song_until_input()
