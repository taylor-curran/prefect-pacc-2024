from prefect import task, flow
import requests

@task
def call_event_webhook():
    # url = "https://api.prefect.cloud/hooks/<your-webhook>"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to call the webhook. Status code: {response.status_code}")

    print("Successfully called the webhook.")
    # You can also process the response here if

@flow
def call_webhook_flow():
    call_event_webhook()

if __name__ == "__main__":
    call_webhook_flow()
