import pyowm

def main():
    lat = 51.5
    lon = -0.116
    api_key = "API_KEY"
    owm = pyowm.OWM(api_key)
    mgr = owm.weather_manager()

    one_call = mgr.one_call(lat=lat, lon=lon)
    
    current_temperature = one_call.current.temperature("celsius")

    temperature = current_temperature.get("temp")
    feels_like = current_temperature.get("feels_like")
    status = one_call.current.status
    detailed_status = one_call.current.detailed_status

    print((
        f"Current Temperature: {temperature}\n"
        f"Feels Like: {feels_like}\n"
        f"{status}\n"
        f"{detailed_status}\n"
    ))

    forecast_daily = one_call.forecast_daily
    
if __name__ == "__main__":
    main()

            
