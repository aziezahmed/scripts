import pyowm
import os

def print_weather(weather):
    temperature = weather.temperature("celsius").get("temp")
    feels_like = weather.temperature("celsius").get("feels_like")

    if(not temperature):
        temperature = weather.temperature("celsius").get("day")
        feels_like = weather.temperature("celsius").get("feels_like_day")
    status = weather.status
    detailed_status = weather.detailed_status
    
    print((f"Weather for {weather.reference_time('iso')}"))
    print((
        f"Temperature: {temperature}\n"
        f"Feels Like: {feels_like}\n"
        f"{status}\n"
        f"{detailed_status}\n"
    ))

def main():
    lat = 51.5
    lon = -0.116
    api_key = os.environ.get("OWM_API_KEY")
    owm = pyowm.OWM(api_key)
    mgr = owm.weather_manager()

    one_call = mgr.one_call(lat=lat, lon=lon)
    print_weather(one_call.current);

    forecast_hourly = one_call.forecast_hourly
    print_weather(forecast_hourly[1])
    print_weather(forecast_hourly[3])
    print_weather(forecast_hourly[5])

    forecast_daily = one_call.forecast_daily
    tomorrows_forecast = forecast_daily[1]
    print_weather(tomorrows_forecast)

if __name__ == "__main__":
    main()

            
