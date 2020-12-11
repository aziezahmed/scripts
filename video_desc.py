import googleapiclient.discovery
import json
import os

def main():

    video_id = "VIDEO_ID"

    api_service_name = "youtube"
    api_version = "v3"
    api_key = os.environ.get("YOUTUBE_API_KEY")

    youtube = googleapiclient.discovery.build(
               api_service_name, 
               api_version, 
               developerKey=api_key)

    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    )
    response = request.execute()

    for video in response["items"]:
        print(video["snippet"]["title"])
        print(video["snippet"]["description"])
 
    
if __name__ == "__main__":
    main()
