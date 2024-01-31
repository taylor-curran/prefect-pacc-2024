from prefect import flow
from prefect.events.schemas import DeploymentTrigger


@flow(log_prints=True)
def downstream_event_triggered_flow(prev_result: str) -> str:
    print(f"got {prev_result=!r}")


downstream_deployment_trigger = DeploymentTrigger(
    name="Wait for Upstream Flow's Result PACC Taylor",
    enabled=True,
    match_related={ # match the flow id of the upstream flow
        "prefect.resource.id": "prefect.flow.00afd929-5829-4e60-934f-e4b51d268fd6"
    },
    # Expect is the main argument of the trigger object
    # The string matches the event name of our emitted event
    expect={"prefect.result.produced"}, 
    # Here we take from the emitted event's payload and apply it to the flow's parameter
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
