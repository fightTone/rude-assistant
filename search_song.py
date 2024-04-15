import os
import googleapiclient.discovery
from get_credentials import get_creds

# Set up the YouTube Data API client
api_service_name = "youtube"
api_version = "v3"
api_key = get_creds(api_service_name)  # Replace with your own API key
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

def search_youtube_and_play(song_title):
    # Call the search endpoint of the YouTube Data API
    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=song_title,
        type="video"
    )
    response = request.execute()
    
    # Extract the video ID from the response
    if 'items' in response and len(response['items']) > 0:
        video_id = response['items'][0]['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        os.system(f"start {video_url}")
    else:
        print("No videos found for the given search query.")

if __name__ == "__main__":
    song_title = input("Enter the title of the song: ")
    search_youtube_and_play(song_title)
