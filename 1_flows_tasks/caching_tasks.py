from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta
from prefect_gcp.cloud_storage import GcsBucket

# Task results can be cached
# Provide a cache_key_fn AND/OR a cached_expiration timedelta to the task decorator
# Docs: https://docs.prefect.io/latest/concepts/tasks/#caching


@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(minutes=1))
def hello_task(name_input):
    print(f"Hello {name_input}!")


@flow
def hello_flow(name_input):
    hello_task(name_input)


# Remote persistence of task results is recommended though optional
# Use a prefect block to specify a GCS bucket to store results
# Docs: https://docs.prefect.io/latest/concepts/results/#result-storage-location
# Docs: https://prefecthq.github.io/prefect-gcp/blocks_catalog/#cloud-storage-module


@flow(result_storage=GcsBucket(bucket="my-block-name"))
def flow_with_remotely_persisted_results(name_input):
    hello_task(name_input)


if __name__ == "__main__":
    hello_flow("Marvin")
