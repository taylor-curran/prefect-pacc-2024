from prefect import flow


@flow(log_prints=True)
def decorated_fn(param_1: str):
    print(param_1)


if __name__ == "__main__":
    decorated_fn.deploy(
        name="my-deployment",
        work_pool_name="docker-pool",
        image="taycurran/prefect-webhook-triggered-flow:latest",
        triggers=[
            {
                "type": "event",
                "match": {"prefect.resource.name": "Updated Regression Model"},
                "match_related": {},
                "after": [],
                "expect": ["model.refreshed"],
                "for_each": [],
                "posture": "Reactive",
                "threshold": 1,
                "within": 0,
                "parameters": {"param_1": "{{ event.resource.id }}"}
            }
        ],
    )
