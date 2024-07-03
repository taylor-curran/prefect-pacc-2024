from prefect import flow
from prefect.events.schemas import DeploymentTrigger
# from prefect.events import DeploymentEventTrigger, DeploymentCompoundTrigger
# TODO Change the script to use DeploymentEventTrigger, DeploymentCompoundTrigger


@flow(log_prints=True)
def downstream_failure_handling_flow(my_prev_flow_run_id):
    print(f"✨ Flow run ID here: {str(my_prev_flow_run_id)}")
    print("I can do failure handling stuff in this flow!")


downstream_deployment_trigger = DeploymentTrigger(
    name="Failure Clean Up",
    enabled=True,
    match_related={  # match the flow name of the upstream flow or don't include this if you want this trigger to be more globally applied
        "prefect.resource.role": "flow",
        "prefect.resource.name": "this-flow-fails",
    },
    # Expect is the main argument of the trigger object, this matches the event name of our emitted event
    expect={"prefect.flow-run.Failed"},
    # Here we take from the emitted events resource information and apply it to the flow's parameter
    parameters={
        "my_prev_flow_run_id": "{{event.resource.id}}",
    },
)

if __name__ == "__main__":
    downstream_failure_handling_flow.deploy(
        name="downstream_failure_handling_flow",
        triggers=[downstream_deployment_trigger],
        work_pool_name="my-k8s-pool",
        image="my-custom-image:latest",
        push=False,
    )
