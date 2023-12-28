from prefect import flow, get_run_logger

# Custom logs can be added inside of flows and tasks
# Docs: https://docs.prefect.io/latest/guides/logs/#prefect-loggers


@flow(name="log-example-flow")
def log_it():
    logger = get_run_logger()
    logger.info("INFO level log message.")
    logger.debug("You only see this message if the logging level is set to DEBUG. 🙂")

# Optionally log all print statements during development
@flow(name="my-dev-flow", log_prints=True)
def dev_flow():
    print("This print statement will be logged.")

if __name__ == "__main__":
    log_it()
