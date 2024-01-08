
Create a webhook and call it from inside a flow
Create a custom event

State change hooks
# Custom Events, Event Webhooks, and State Change Hooks Quickstart

There are two ways to get things that happen outside of Prefect into your workspace's event feed, Event Webhooks, and Custom Emitted Events.

### Create and call an [Event Webhook](https://docs.prefect.io/latest/guides/webhooks/).
1. Find the Event Webhooks page and create an Event Webhook.
    ![Alt text](create_webhook.png)
2. Copy the Webhook URL and call the endpoint from a Prefect task:
    
    Something like:
    ```python
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
    ```

# [State Change Hooks](https://docs.prefect.io/latest/concepts/states/#state-change-hooks)