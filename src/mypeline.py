from src.subpackage.other_module import some_helper_function
from clearml import Task


my_task = Task.init(
    project_name="examples",
    task_name="dummy task",
)

if __name__ == "__main__":
    my_task.execute_remotely(
        queue_name="default",
        clone=False,
        exit_process=True,
    )
    print("Hello World!")
    some_helper_function("main task")
