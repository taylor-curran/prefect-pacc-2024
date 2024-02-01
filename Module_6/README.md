# Advanced Subflow Patterns

1. Use [`run_deployment`](https://docs.prefect.io/latest/api-ref/prefect/deployments/deployments/#prefect.deployments.deployments.run_deployment) inside of a flow to create a sub flow that has its own infrastructure.

```python
from prefect.deployments import run_deployment
from prefect import flow

@flow
def main():
    run_deployment(name="my_flow_name/my_deployment_name")
```