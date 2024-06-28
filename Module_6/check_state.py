import time

from prefect import flow, task, get_client
from prefect.client.schemas.filters import (
    FlowRunFilter,
    DeploymentFilter,
    DeploymentFilterId,
    FlowRunFilterState,
    FlowRunFilterStateType,
)
from prefect.client.schemas.objects import StateType
from prefect.runtime import deployment
from prefect.states import Cancelled


@flow(log_prints=True)
def skip_example():
    if deployment_already_running():
        return Cancelled()

    else:
        time.sleep(30)  # do other stuff


@task
async def deployment_already_running() -> bool:
    deployment_id = deployment.get_id()
    async with get_client() as client:
        # find any running flows for this deployment
        running_flows = await client.read_flow_runs(
            deployment_filter=DeploymentFilter(
                id=DeploymentFilterId(any_=[deployment_id])
            ),
            flow_run_filter=FlowRunFilter(
                state=FlowRunFilterState(
                    type=FlowRunFilterStateType(any_=[StateType.RUNNING])
                ),
            ),
        )
    if len(running_flows) > 1:
        return True

    else:
        return False
