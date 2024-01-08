import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

@task
def call_prefect_webhook():
    # Get the webhook URL from the environment variable
    url = os.getenv("PREFECT_WEBHOOK_URL")

    if not url:
        raise ValueError("Webhook URL not found in environment variables")

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to call the webhook. Status code: {response.status_code}")

    print("Successfully called the webhook.")
    # You can also process the response here if needed