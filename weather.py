import pyowm

def main():
    lat = 51.5
    lon = -0.116
    api_key = "API_KEY"
    owm = pyowm.OWM(api_key)
    mgr = owm.weather_manager()

    one_call = mgr.one_call(lat=lat, lon=lon)
    
    print(one_call.current.temperature())
    
if __name__ == "__main__":
    main()

            
