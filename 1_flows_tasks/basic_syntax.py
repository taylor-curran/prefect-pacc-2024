import httpx  # requests capability, but can work with async
from prefect import flow, task

# Tasks run inside flows.
# Flows are the main unit of execution in Prefect, they can be scheduled
# Docs: https://docs.prefect.io/latest/concepts/flows/#writing-flows
# Docs: https://docs.prefect.io/latest/concepts/tasks/#tasks-overview


@task
def fetch_weather(lat: float, lon: float):
    base_url = "https://api.open-meteo.com/v1/forecast/"
    weather = httpx.get(
        base_url,
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    most_recent_temp = float(weather.json()["hourly"]["temperature_2m"][0])
    return most_recent_temp


# Tasks can't run inside other tasks.
@task
def save_weather(temp: float):
    with open("weather.csv", "w+") as w:
        w.write(str(temp))
    return "Successfully wrote temp"


# Flows CAN run inside other flows.
# Docs: https://docs.prefect.io/latest/concepts/flows/#composing-flows
@flow
def my_subflow():
    return "Flows can run inside other flows"


@flow
def pipeline(lat: float = 38.9, lon: float = -77.0):
    temp = fetch_weather(lat, lon)
    result = save_weather(temp)
    subflow_result = my_subflow()
    return {"weather": result, "subflow": subflow_result}


if __name__ == "__main__":
    pipeline()
