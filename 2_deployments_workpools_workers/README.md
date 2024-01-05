# Deployment Quickstart

![Alt text](main_diagram.png)
For conceptual breakdown of the diagram, go to [Architecture Diagrams Walkthrough](archetecture_diagrams_walkthrough.md).

### 1. [Create a work pool](https://docs.prefect.io/latest/tutorial/workers/#create-a-work-pool) or choose one that already exists in your workspace.
_**Creating a work pool in the UI**_ is recommended for your first go so you get a sense of all the options.

To see any existing work pools:
```bash
prefect work-pool ls
``` 

Otherwise you can create a work pool with the following command:
```bash
prefect work-pool create "my-pool" --type docker
```
(https://docs.prefect.io/latest/tutorial/workers/#start-a-worker)

### 2. [Start a worker](https://docs.prefect.io/latest/tutorial/workers/#start-a-worker) to poll this work pool.

pip install the required library
```python
pip install prefect-docker
```

On your laptop, open up a new terminal, activate your python environment, and type:
```bash
prefect worker start --pool my-docker-pool
```
^Keep this guy running for as long as you want to run deployments on your laptop. Go to our [guides]() when you are ready to start a worker in a production environment (aka not on your laptop)

### 3. Now you're all set [create a deployment](https://docs.prefect.io/latest/tutorial/workers/#create-the-deployment) to send your flow to your work pool.


1. Start your docker daemon.
2. Use the flow.deploy() method to create a deployment:


    ```python
    import httpx
    from prefect import flow


    @flow(log_prints=True)
    def my_flow():
        print("Hello World!")

    if __name__ == "__main__":
        my_flow.deploy(
            name="janes-pacc-deployment", 
            work_pool_name="my-docker-work-pool", 
            image="my-first-deployment-image:pacc",
            push=False
        )
    ```

