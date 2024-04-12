from prefect import flow


@flow(log_prints=True)
def hello_world():
    print("Hello world!")


if __name__ == "__main__":
    hello_world()
