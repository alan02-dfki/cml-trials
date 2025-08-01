from src.subpackage.other_module import the_actual_business_logic
from clearml import Task


my_task = Task.init(
    project_name="examples",
    task_name="dummy task",
)

if __name__ == "__main__":
    print("This is visible on both the local and the remote machine!")
    my_task.execute_remotely(
        queue_name="default",
        clone=False,
        exit_process=True,
    )
    print("This is only visible the remote machine!")

    the_actual_business_logic("main task")
