import httpx
from prefect import flow, task
from prefect.artifacts import create_markdown_artifact

# Artifacts are a way to post information about a flow run to Prefect
# I like to think of artifacts as the "custom tab" of a flow run page in the UI
# Docs: https://docs.prefect.io/latest/concepts/artifacts/


@task
def mark_it_down(temp):
    markdown_report = f"""# Weather Report
    
## Recent weather

| Time        | Temperature |
|:--------------|-------:|
| Now | {temp} |
| In 1 hour       | {temp + 2} |
"""
    create_markdown_artifact(
        key="weather-report",
        markdown=markdown_report,
        description="Very scientific weather report",
    )


@flow
def fetch_weather(lat: float, lon: float):
    base_url = "https://api.open-meteo.com/v1/forecast/"
    weather = httpx.get(
        base_url,
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    most_recent_temp = float(weather.json()["hourly"]["temperature_2m"][0])
    mark_it_down(most_recent_temp)


if __name__ == "__main__":
    fetch_weather(38.9, -77.0)
