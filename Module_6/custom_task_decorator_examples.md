These code examples demonstrate how to implement task skipping by customizing task and flow behavior. 

Origianlly posted in [this gh issue](https://github.com/PrefectHQ/prefect/issues/9347#issuecomment-1532186528) by Zanie.

---

First Code Block: Avoid Submission of Tasks by Passing `skip_tasks` Around** 

```Copy code
from typing import List
from prefect import Flow, Task, flow
from prefect.states import Completed
import functools

def task(__fn=None, **kwargs):
    if __fn:
        return CustomTask(fn=__fn, **kwargs)
    else:
        return functools.partial(task, **kwargs)

class CustomTask(Task):
    def submit(self, *args, **kwargs):
        skip_tasks = kwargs.pop("skip_tasks", [])
        if self.name in skip_tasks:
            return None  # Skip submission
        return super().submit(*args, **kwargs)

@task
def foo():
    print("foo")

@task
def bar():
    print("bar")

@flow
def my_flow_from_direct(skip_tasks: List[str] = []):
    foo.submit(skip_tasks=skip_tasks)
    bar.submit(skip_tasks=skip_tasks)

my_flow_from_direct(skip_tasks=["foo"])
```
**Explanation:**  
- **Custom Task Decorator and Class:**  
  - A custom `task` decorator wraps Prefect's `Task` class to return instances of `CustomTask` instead of the default `Task`.
 
  - `CustomTask` overrides the `submit` method to check if the task's name is in the `skip_tasks` list.
 
- **Skipping Logic:**  
  - If the task's name is in `skip_tasks`, `submit` returns `None`, effectively skipping the task submission.
 
  - If not, it calls the superclass's `submit` method to proceed as usual.
 
- **Flow Implementation:**  
  - In `my_flow_from_direct`, tasks `foo` and `bar` are submitted with the `skip_tasks` parameter.
 
  - When `my_flow_from_direct(skip_tasks=["foo"])` is called, the `foo` task is skipped, and `bar` executes normally.
**How It Addresses the Feature Request:** 
- Allows skipping tasks dynamically by specifying their names in a list.

- Avoids the need for state change hooks or modifying task functions.

- Enables data engineers to control task execution externally.


---

**Second Code Block: Avoid Submission of Tasks Using a Context Variable** 

```Copy code
from contextvars import ContextVar

_SKIP_TASKS = ContextVar("skip_tasks", default=[])

def task(__fn=None, **kwargs):
    if __fn:
        return CustomTask(fn=__fn, **kwargs)
    else:
        return functools.partial(task, **kwargs)

class CustomTask(Task):
    def submit(self, *args, **kwargs):
        skip_tasks = _SKIP_TASKS.get()
        if self.name in skip_tasks:
            return None  # Skip submission
        return super().submit(*args, **kwargs)

class CustomFlow(Flow):
    def __call__(self, *args, **kwargs):
        skip_tasks = kwargs.pop("skip_tasks", [])
        token = _SKIP_TASKS.set(skip_tasks)
        try:
            retval = super().__call__(*args, **kwargs)
        finally:
            _SKIP_TASKS.reset(token)
        return retval

def flow(__fn=None, **kwargs):
    if __fn:
        return CustomFlow(fn=__fn, **kwargs)
    else:
        return functools.partial(flow, **kwargs)

@flow
def my_flow_from_context():
    foo.submit()
    bar.submit()

my_flow_from_context(skip_tasks=["foo"])
```
**Explanation:**  
- **Context Variable `_SKIP_TASKS`:**  
  - Uses Python's `contextvars.ContextVar` to store the `skip_tasks` list globally within the context of the flow execution.
 
- **Custom Task and Flow Classes:**  
  - `CustomTask.submit` retrieves `skip_tasks` from the context variable.
 
  - `CustomFlow.__call__` sets the `skip_tasks` context variable before the flow runs and resets it afterward.
 
- **Flow Implementation:**  
  - Tasks are submitted without explicitly passing `skip_tasks`.

  - The context variable determines whether a task should be skipped.
**How It Addresses the Feature Request:**  
- Provides a cleaner interface by eliminating the need to pass `skip_tasks` to each task.

- Centralizes task-skipping logic using a context variable.

- Allows skipping tasks without modifying the flow's internal task submissions.


---

**Third Code Block: Skipping Tasks After Creation Using a Wrapper Function** 

```Copy code
def task(__fn=None, **kwargs):
    if __fn:
        return CustomTask(fn=my_task_wrapper(__fn), **kwargs)
    else:
        return functools.partial(task, **kwargs)

def my_task_wrapper(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        skip_tasks = _SKIP_TASKS.get()
        if fn.__name__ in skip_tasks:
            return Completed(name="Skipped")  # Mark as skipped
        return fn(*args, **kwargs)
    return wrapper

@task
def foo_wrapped():
    print("foo")

@task
def bar_wrapped():
    print("bar")

@flow
def my_flow_return_skipped():
    foo_wrapped.submit()
    bar_wrapped.submit()

my_flow_return_skipped(skip_tasks=["foo_wrapped"])
```
**Explanation:**  
- **Task Function Wrapper:**  
  - `my_task_wrapper` wraps the task function to insert skipping logic.
 
  - Checks if the task's name is in `skip_tasks` and returns a `Completed` state named "Skipped" if so.
 
- **Custom Task Decorator:** 
  - Applies the wrapper to each task function.
 
- **Flow Implementation:** 
  - Tasks are submitted as usual.

  - Skipping is handled within the task execution.
**How It Addresses the Feature Request:** 
- Skips tasks after their task runs are created but before execution.

- Marks skipped tasks explicitly, which can be useful for logging or monitoring.
 
- Doesn't prevent task submission but alters task execution based on `skip_tasks`.


---

**Fourth Code Block: Skipping Tasks and Propagating to Downstream Tasks** 

```Copy code
class SKIPPED:
    pass

def task(__fn=None, **kwargs):
    if __fn:
        return CustomTask(fn=my_task_wrapper(__fn), **kwargs)
    else:
        return functools.partial(task, **kwargs)

def my_task_wrapper(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        skip_tasks = _SKIP_TASKS.get()
        if fn.__name__ in skip_tasks or SKIPPED in args or SKIPPED in kwargs.values():
            return Completed(name="Skipped", data=SKIPPED)
        return fn(*args, **kwargs)
    return wrapper

@task
def foo_wrapped():
    print("foo")

@task
def bar_wrapped(x):
    print("bar")

@flow
def my_flow_return_skipped_with_downstream():
    upstream = foo_wrapped()
    bar_wrapped(upstream)

my_flow_return_skipped_with_downstream(skip_tasks=["foo_wrapped"])
```
**Explanation:**  
- **Custom `SKIPPED` Class:** 
  - Acts as a marker to indicate that a task was skipped.
 
- **Wrapper Function Enhancement:**  
  - Checks if any input arguments are `SKIPPED`.
 
  - If so, skips the task and returns a `Completed` state with `data=SKIPPED`.
 
- **Propagating Skips to Downstream Tasks:**  
  - When `foo_wrapped` is skipped, it returns `SKIPPED`.
 
  - `bar_wrapped` receives `SKIPPED` as input and is also skipped.
**How It Addresses the Feature Request:** 
- Allows skipping tasks and automatically skips dependent downstream tasks.

- Provides a mechanism to propagate the skipped state through the task dependencies.

- Useful for complex flows where skipping a task should affect subsequent tasks.


---

**Overall, these code examples address the feature request by:**  
- **Customizing Task and Flow Behavior:**  
  - By extending or wrapping Prefect's `Task` and `Flow` classes, you can insert custom logic to control task execution.
 
- **Dynamic Task Skipping:** 
  - Allows tasks to be skipped based on runtime parameters or conditions without altering the core flow logic.
 
- **Avoiding State Change Hooks:** 
  - Since state change hooks aren't designed to mutate state transitions or prevent task execution, these methods provide alternative solutions.
 
- **Minimal Changes to Existing Code:** 
  - The task and flow decorators can be applied without significant refactoring, making it practical for integration into existing projects.
**In summary,**  the code demonstrates how to implement task skipping in Prefect flows by customizing task submission and execution. It provides practical examples of how data engineers can control which tasks to run or skip, addressing the original feature request without relying on state change hooks that aren't suitable for this purpose.
If you have any specific questions about any part of the code or need further clarification on how it works within the Prefect framework, feel free to ask!
