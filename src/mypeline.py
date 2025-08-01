from clearml import Task


my_task = Task.init(
    project_name="examples",
    task_name="dummy task",
)

if __name__ == "__main__":
    # my_task.execute_remotely(
    #     queue_name="default",  # type: Optional[str]
    #     clone=False,  # type: bool
    #     exit_process=True,  # type: bool
    # )
    print("Hello World!")
