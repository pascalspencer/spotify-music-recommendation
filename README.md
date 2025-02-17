# Spotify Recommendation App using Spotipy & Kivy

This project is a simple music recommendation app that integrates Spotify API using `Spotipy` and provides a graphical interface with `Kivy`. The app fetches user-specific top tracks, recently played tracks, and generates recommendations based on danceability.

## Features
- Fetch user's top 10 tracks
- Retrieve the most recently played track
- Generate song recommendations based on recently played tracks with high danceability
- Interactive GUI built with Kivy

## Requirements
Ensure you have Python installed and install the required dependencies:
```sh
pip install spotipy kivy
```

## Setup
1. Register a Spotify Developer Account and create an app to obtain credentials from [Spotify Developer Dashboard](https://developer.spotify.com/).
2. Set up your credentials in the script:
    ```python
    client_id = "your_client_id"
    client_secret = "your_client_secret"
    redirect_uri = "your_redirect_uri"
    ```
3. Clone the repository:
    ```sh
    git clone https://github.com/your-username/spotify-kivy-app.git
    cd spotify-kivy-app
    ```
4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
Run the script using:
```sh
python app.py
```

## Notes
- Ensure your Spotify account has the required permissions to access top tracks and recently played tracks.
- The app currently focuses on danceability-based recommendations but can be extended for other parameters.

## License
This project is licensed under the MIT License.

