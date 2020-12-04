import googleapiclient.discovery
import json
import os

def main():

    channel_name = "CHANNEL_NAME"
    api_service_name = "youtube"
    api_version = "v3"
    api_key = os.environ.get("YOUTUBE_API_KEY")

    youtube = googleapiclient.discovery.build(
               api_service_name, 
               api_version, 
               developerKey=api_key)

    request = youtube.search().list(
        part="snippet",
        maxResults=5,
        type="channel",
        q=channel_name
    )
    response = request.execute()

    channel_id = response["items"][0]["id"]["channelId"]

    request = youtube.search().list(
        part="snippet,id",
        maxResults=20,
        channelId=channel_id,
        order="date",
        type="video"
    )
    
    response = request.execute()

    for video in response["items"]:
        print(video["snippet"]["title"])
        print(f"https://www.youtube.com/watch?v={video['id']['videoId']}\n")
    
if __name__ == "__main__":
    main()
