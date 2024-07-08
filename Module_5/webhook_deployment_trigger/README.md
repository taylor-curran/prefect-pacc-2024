# Example

Create a dynamic webhook

![alt text](images/create_webhook.png)

```bash
curl -X POST 'https://api.prefect.cloud/hooks/u<redacted>w' -H "Content-Type: application/json" -d '{"event_name": "model.refreshed", "model": "regression_v2", "friendly_name": "Updated Regression Model"}'
```
