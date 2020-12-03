import googleapiclient.discovery
import json


def main():

    search_term = "SEARCH_TERM"
    api_service_name = "youtube"
    api_version = "v3"
    api_key = "API_KEY"
    
    youtube = googleapiclient.discovery.build(
               api_service_name, 
               api_version, 
               developerKey=api_key)

    request = youtube.search().list(
        part="snippet,id",
        maxResults=5,
        q=search_term,
        type="video"
    )
    response = request.execute()

    for video in response["items"]:
        print(video["snippet"]["title"])
        print(f"https://www.youtube.com/watch?v={video['id']['videoId']}\n")
    
if __name__ == "__main__":
    main()
