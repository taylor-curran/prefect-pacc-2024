from prefect import flow, pause_flow_run


@flow(log_prints=True)
def greet_user():
    name = pause_flow_run(str)
    print(f"Hello, {name}!")


if __name__ == "__main__":
    greet_user()
