from prefect import flow


@flow
def this_flow_fails():
    print("This flow will fail")
    raise ValueError("This flow failed")


if __name__ == "__main__":
    this_flow_fails()
