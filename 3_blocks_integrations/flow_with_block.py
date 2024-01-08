from prefect import flow, task
from prefect.blocks.system import JSON

@task
def load_block():
    jb = JSON.load("taylor-pacc-json-block")
    my_dict = jb.value

    print(my_dict)

@flow(log_prints=True)
def load_block_flow():
    load_block()

if __name__ == "__main__":
    load_block_flow()