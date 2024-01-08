from prefect import flow

@flow(log_prints=True)
def my_flow(name: str = "World"):
    print(f"Hello {name}!")


if __name__ == "__main__":

    my_flow.deploy(
        name="taylor-pacc-deployment",
        work_pool_name="my-k8s-pool",
        image="docker.io/taycurran/pacc:demo",
        push=False,
        tags=["pacc", "taylor"],
    )