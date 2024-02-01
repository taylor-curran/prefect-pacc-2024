import httpx  # requests capability, but can work with async
from prefect import flow, task

# Multiple tasks can be run concurrently if the submit method is used
# Docs: https://docs.prefect.io/latest/tutorial/tasks/#concurrency


@task
def fetch_temperature(lat: float, lon: float):
    base_url = "https://api.open-meteo.com/v1/forecast/"
    weather = httpx.get(
        base_url,
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    most_recent_temp = float(weather.json()["hourly"]["temperature_2m"][0])
    return most_recent_temp


@task
def celsius_to_fahrenheit(celsius_temp):
    fahrenheit_temp = (celsius_temp * 9.0 / 5.0) + 32
    return fahrenheit_temp


@task
def fetch_wind_speed(lat: float, lon: float):
    base_url = "https://api.open-meteo.com/v1/forecast/"
    weather = httpx.get(
        base_url,
        params=dict(latitude=lat, longitude=lon, hourly="windspeed_10m"),
    )
    most_recent_wind_speed = float(weather.json()["hourly"]["windspeed_10m"][0])
    return most_recent_wind_speed


@flow
def pipeline(lat: float = 38.9, lon: float = -77.0):
    temp = fetch_temperature.submit(lat, lon)
    # task celsius_to_fahrenheit is dependent on task fetch_temperature
    # prefect detects this dependency through the result of temp being passed
    temp_f = celsius_to_fahrenheit.submit(temp)
    wind_speed = fetch_wind_speed.submit(lat, lon)
    return dict(
        temp=temp_f,
        wind_speed=wind_speed,
    )


if __name__ == "__main__":
    pipeline()
