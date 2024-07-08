# Example

Create a dynamic webhook

![alt text](images/create_webhook.png)

```json
{
    "event": "{{body.event_name}}",
    "resource": {
        "prefect.resource.id": "product.models.{{ body.model }}",
        "prefect.resource.name": "{{ body.friendly_name }}",
        "producing-team": "Data Science"
    }
}
```


```bash
curl -X POST 'https://api.prefect.cloud/hooks/u<redacted>w' -H "Content-Type: application/json" -d '{"event_name": "model.refreshed", "model": "regression_v2", "friendly_name": "Updated Regression Model"}'
```
