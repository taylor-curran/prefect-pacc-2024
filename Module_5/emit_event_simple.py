from prefect.events import emit_event


def some_function(name: str = "kiki") -> None:
    print(f"hi {name}!")
    emit_event(
        event=f"{name}.sent.event!", resource={"prefect.resource.id": f"coder.{name}"}
    )


some_function()
