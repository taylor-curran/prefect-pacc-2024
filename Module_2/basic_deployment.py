from prefect import flow


@flow(log_prints=True)
def my_flow(name: str = "World"):
    print(f"Hello {name}!")


if __name__ == "__main__":
    my_flow.deploy(
        name="taylor-pacc-deployment",
        work_pool_name="taylor-pacc-work-pool",
        image="docker.io/taycurran/pacc:quickstart",
        push=False,
        tags=["pacc", "taylor"],
        interval=3000,
    )
