from prefect import flow
from prefect.runner.storage import GitRepository, GitCredentials
import os

from prefect.filesystems import GitHub

# TODO -- all this needs to be updated
# Docs for Remote Storage: https://docs.prefect.io/latest/guides/deployment/storage-guide/#where-to-store-your-flow-code
# Docs Docker Based Storage: https://docs.prefect.io/latest/guides/deployment/storage-guide/#option-3-docker-based-storage
# Docs GCP Based Storage: https://docs.prefect.io/latest/guides/deployment/storage-guide/#__tabbed_3_3

# TODO: Add scheduling


@flow(log_prints=True)
def my_flow(name: str = "World"):
    print(f"Hello {name}!")


if __name__ == "__main__":
    # my_flow.from_source(
    #     source=GitHub.load("my-private-gh-block"),
    #     entrypoint="child_flows.py:child_flow_d",
    # ).deploy(
    #     name="my-dep-5",
    #     work_pool_name="my-k8s-pool",
    #     image="docker.io/taycurran/child-d:demo",
    #     build=False,
    # )

    # my_flow.from_source(
    #     source=GitHub.load("my-private-gh-block"),
    #     entrypoint="child_flows.py:child_flow_d",
    # ).deploy(
    #     name="my-dep-5",
    #     work_pool_name="my-k8s-pool",
    #     image="docker.io/taycurran/child-d:demo",
    #     build=False,
    #     tags=["my-tag-1", "my-tag-2"],
    # )

    my_flow.deploy(
        name="my-dep-5",
        work_pool_name="my-k8s-pool",
        image="docker.io/taycurran/child-d:demo",
        build=False,
        tags=["pacc", "taylor"],
    )
