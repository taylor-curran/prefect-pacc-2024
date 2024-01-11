# Basic Syntax Quickstart

![Alt text](images/flow_task_diagrams.png)

### Rules of Thumb
- At a minimum, you need to define at least one flow function.
- Your flows can be segmented by introducing task (`@task`) functions, which can be invoked from within these flows.
- A task represents a discrete unit of Python code, whereas flows are more akin to parent functions accommodating a broad range of workflow logic.
- Flows can be called inside of other flows (we call these subflows) but a task **cannot** be run inside of another task or from outside the context of a flow.

## Module 1 Lab

1. Create your first flows and tasks modeled off the [basic-syntax](basic_syntax.py) script.
    - Run your flow locally and verify that the flow run shows up in the UI. 
    - Head to the `Flow Runs` page in the UI and click on the animal-adjective flow run name to see your flow run page.
    ![Alt text](images/animal_adj.png)
2. Try adding [caching](caching_tasks.py) and [retries](retries.py) to your tasks and flows.
    - Verify that the tasks show up in a cached state.
    - Head to the `Task Runs` tab of the flow run page.
    ![Alt text](images/flow_run_tabs.png)
3. Add a [custom log](custom_logs.py).
    - Verify that this log shows up in the UI.
    - Check out the logs in the `Logs` tab of the flow run page.
4. Optional: Generate an [artifact](prefect_artifact.py) in one of your tasks or flows.
    - Verify that the artifact shows up in the Artifacts tab of the flow run page.
