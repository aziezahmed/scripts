from astral import LocationInfo
from datetime import datetime
from astral.sun import sunrise, dawn, noon, dusk, sunset

city = LocationInfo("London", "England", "Europe/London", 51.5, -0.116)

print((
        f"Information for {city.name}/{city.region}\n"
        f"Timezone: {city.timezone}\n"
        f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n"
    ))

today = datetime.today()
observer = city.observer

timeformat = "%H:%M:%S"

dawnAngle = 18.0
duskAngle = 18.0

dawn = datetime.fromtimestamp(dawn(observer, today, dawnAngle).timestamp()).strftime(timeformat)
sunrise = datetime.fromtimestamp(sunrise(observer, today).timestamp()).strftime(timeformat)
noon = datetime.fromtimestamp(noon(observer, today).timestamp()).strftime(timeformat)
sunset = datetime.fromtimestamp(sunset(observer, today).timestamp()).strftime(timeformat)
dusk = datetime.fromtimestamp(dusk(observer, today, duskAngle).timestamp()).strftime(timeformat)

print((
        f"Dawn: {dawn}\n"
        f"Sunrise: {sunrise}\n"
        f"Noon: {noon}\n"
        f"Sunset: {sunset}\n"
        f"Dusk: {dusk}\n"
    ))
