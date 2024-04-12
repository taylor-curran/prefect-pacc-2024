from prefect import flow
from prefect.events.schemas import DeploymentTrigger


@flow(log_prints=True)
def downstream_event_triggered_flow(prev_result: str) -> str:
    print(f"got {prev_result=!r}")


downstream_deployment_trigger = DeploymentTrigger(
    name="Wait for Upstream Flow's Result PACC Taylor",
    enabled=True,
    match_related={  # match the flow name of the upstream flow
        "prefect.resource.role": "flow",
        "prefect.resource.name": "upstream-flow",
    },
    # Expect is the main argument of the trigger object, this matches the event name of our emitted event
    expect={"prefect.result.produced"},
    # Here we take from the emitted events payload and apply it to the flows parameter
    parameters={
        "prev_result": "{{event.payload.result}}",
    },
)

if __name__ == "__main__":
    downstream_event_triggered_flow.deploy(
        name="taylor-pacc-trigger",
        work_pool_name="my-k8s-pool",
        image="my-second-deployment-image:pacc",
        push=False,
        tags=["pacc", "taylor"],
        triggers=[downstream_deployment_trigger],
    )
