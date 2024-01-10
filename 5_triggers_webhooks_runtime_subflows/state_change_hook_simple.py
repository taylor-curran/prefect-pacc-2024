from prefect import flow


def my_success_hook(flow, flow_run, state):
    print(state.type)
    print(state.result())
    print(flow_run.name)
    print(flow_run.start_time)
    print(flow.name)
    print("Flow run succeeded!")


@flow(on_completion=[my_success_hook])
def my_flow():
    return 42


my_flow()
