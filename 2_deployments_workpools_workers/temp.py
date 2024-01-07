from prefect.blocks.notifications import SlackWebhook

slack_webhook_block = SlackWebhook.load("my-block-name")
slack_webhook_block.notify("Hello from Prefect!")

# TODO: blocks lab
