import httpx
from prefect import flow, task

# Flows and tasks can be retried on failure
# Optionally provide a retry_delay_seconds to the decorator
# Docs: https://docs.prefect.io/latest/concepts/tasks/#retries
# Docs: https://docs.prefect.io/latest/concepts/flows/#flow-settings


@task(retries=4, retry_delay_seconds=0.1)
def fetch_cat_fact():
    cat_fact = httpx.get("https://httpstat.us/Random/200,500", verify=False)
    if cat_fact.status_code >= 400:
        raise Exception()
    print(cat_fact.text)


@flow
def fetch():
    fetch_cat_fact()


if __name__ == "__main__":
    fetch()
