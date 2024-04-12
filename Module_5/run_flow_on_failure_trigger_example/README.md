# Run Flow on Failure Trigger Example

This directory showcases an advanced Prefect example where one flow is intentionally designed to fail (`upstream_failing_flow.py`), and upon its failure, another flow (`trigger_on_failure.py`) is automatically triggered. Importantly, the run ID of the failing flow is passed as an argument to the downstream failure handling flow, enabling targeted and intelligent failure handling or cleanup operations.
## Scripts Overview 
- `upstream_failing_flow.py`: Defines a Prefect flow named `this_flow_fails` that simulates a flow failure by intentionally raising a `ValueError`. This script acts as the upstream flow whose failure triggers the execution of the downstream flow defined in the other script. 
- `trigger_on_failure.py`: Implements a Prefect flow called `downstream_failure_handling_flow`, which is designed to be executed in response to the failure of the upstream flow. A `DeploymentTrigger` named "Failure Clean Up" is specifically configured to target the failure of `this_flow_fails`. Crucially, this trigger is designed to pass the `run ID` of the failed upstream flow to the downstream flow as an argument, facilitating specific failure handling or cleanup procedures. This flow is prepared for deployment with a designated Kubernetes pool and a specified Docker image.
## Setup and Execution Instructions 
1. Ensure Prefect is installed in your environment. If necessary, install Prefect using pip:

    ```bash
    pip install prefect
    ``` 
2. Start by deploying the `downstream_failure_handling_flow` and setting up its trigger by executing:

    ```bash
    python trigger_on_failure.py
    ```



    This step establishes the failure trigger and readies the flow for deployment with specified details such as the Kubernetes pool and Docker image. 
3. Following the deployment and trigger setup of the downstream flow, simulate a failure scenario by running the `upstream_failing_flow.py` locally. This action will trigger the downstream flow, demonstrating the passing of the failing flow's run ID as an argument:

    ```bash
    python upstream_failing_flow.py
    ```
    The intentional failure of this script will activate the downstream flow, employing the passed run ID for targeted failure handling.

## Key Component

The passing of the failing flow's run ID to the downstream flow is a critical aspect of this example, enabling precise and context-aware failure handling mechanisms within Prefect flows. Adjust the `DeploymentTrigger` configurations and deployment details in `trigger_on_failure.py` as needed to align with your specific environmental requirements and use cases.
