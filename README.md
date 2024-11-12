# Spotify Skipping Bot
A Python bot that automatically skips songs on Spotify after one minute of playback to enhance your listening experience.

## Features
- Automatically skips songs after 1 minute of playtime.
- Continuously skips songs until the song is paused. After the song is paused, the bot stops.
- Built using Python and the Spotipy library for Spotify API integration.

## Prerequisites
Before you begin, ensure you have met the following requirements:

- Python 3.10 or higher installed.
- A Spotify Developer account to create an app and obtain credentials.
- The Spotipy library installed. You can install it using pip:

```bash
pip install spotipy
```

- Open the `SkippingBot.py` file.
- Locate the following lines and replace the placeholder text with your actual Spotify API credentials:

```python
CLIENT_ID = 'YOUR_CLIENT_ID'         # Your Spotify Client ID
CLIENT_SECRET = 'YOUR_CLIENT_SECRET' # Your Spotify Client Secret
REDIRECT_URI = 'http://localhost:8888/callback'  # Your Redirect URI
```

## License
This project is open-source and licensed under the [MIT License](LICENSE).
