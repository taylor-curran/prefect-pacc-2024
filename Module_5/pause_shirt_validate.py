from typing import Literal
import pydantic
from prefect import flow, pause_flow_run
from prefect.input import RunInput


class ShirtOrder(RunInput):
    """Shirt order options"""

    size: Literal["small", "medium", "large", "xlarge"]
    color: Literal["red", "green", "black"]

    @pydantic.validator("color")
    def validate_shirt(cls, value, values, **kwargs):
        """Validate that shirt combo exists"""

        if value == "green" and values["size"] == "small":
            raise ValueError("We don't carry that combination.")
        return value


@flow(log_prints=True)
def get_shirt_order():
    """Get shirt selection from user via UI"""
    shirt_order = None

    while shirt_order is None:
        try:
            shirt_order = pause_flow_run(wait_for_input=ShirtOrder)
            print(f"We'll send you your shirt in {shirt_order} ASAP!")
        except pydantic.ValidationError:
            print(f"Invalid size and color combination.")


if __name__ == "__main__":
    get_shirt_order()
