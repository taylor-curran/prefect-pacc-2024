from prefect import flow
from prefect.client.schemas.objects import Flow, FlowRun
from prefect.events import emit_event
from prefect.states import State


def emit_on_complete(flow: Flow, flow_run: FlowRun, state: State):
    """State change hook that will run upon the `flow_run` entering a `Completed` state"""
    print(
        f"hello from {flow_run.name}'s completion hook |"
        f" the return value was {(r := state.result())!r}"
    )
    emit_event(
        event="prefect.result.produced",  # this is an arbitrary event name
        resource={"prefect.resource.id": f"prefect.result.{flow.name}.{flow_run.id}"},
        related=[
            {   # This will link the event to the flow that emitted it
                "prefect.resource.id": f"prefect.flow.{flow_run.flow_id}", 
                "prefect.resource.role": "flow",
                "prefect.resource.name": f"{flow.name}",
            }
        ],
        payload={"result": r},
    )


@flow(
    persist_result=True,
    on_completion=[emit_on_complete],
)
def upstream_flow() -> str:
    return "foobar"


if __name__ == "__main__":
    upstream_flow()
