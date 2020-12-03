import requests
import json

def main():
    geo_location_url = 'https://freegeoip.live/json/'
    request = requests.get(geo_location_url)
    location = json.loads(request.text)
    lat = location['latitude']
    lon = location['longitude']

    print((
        f"Latitude: {lat}\n"
        f"Longitude: {lon}\n"
    ))
    
if __name__ == "__main__":
    main()
