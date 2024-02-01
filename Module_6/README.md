# Advanced Subflow Patterns

1. Use [`run_deployment`](https://docs.prefect.io/latest/api-ref/prefect/deployments/deployments/#prefect.deployments.deployments.run_deployment) inside of a flow to create a sub flow that has its own infrastructure.

    Use a deployment you created in [Module 2](../Module_2/README.md).

    ```python
    from prefect.deployments import run_deployment
    from prefect import flow

    @flow
    def main():
        run_deployment(name="my_flow_name/my_deployment_name")
    ```

2. Use [`runtime`](https://docs.prefect.io/latest/guides/runtime-context/#accessing-runtime-information) to get information about your flow run during runtime.

    Try adding a breakpoint inside of your flow... when you hit the breakpoint type `dir(runtime)` or `dir(runtime.deployment)` to see what type of information is available.

    ```python
    from prefect import flow, task
    from prefect import runtime

    @flow(log_prints=True)
    def my_flow(x):
        print("My name is", runtime.flow_run.name)
        breakpoint() ## Add a breakpoint like so
        print("I belong to deployment", runtime.deployment.name)
        my_task(2)

    @task
    def my_task(y):
        print("My name is", runtime.task_run.name)
        print("Flow run parameters:", runtime.flow_run.parameters)

    my_flow(1)
    ```