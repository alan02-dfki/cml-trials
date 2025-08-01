import os

from clearml import Task
from dotenv import load_dotenv

load_dotenv()
token = os.environ["GIT_OAUTH_TOKEN"]
my_task = Task.create(
    project_name="examples",
    task_name="dummy task",
    script="src/mypline",
    add_task_init_call=False,
    repo="git@github.com:alan02-dfki/cml-trials.git",
    # docker="nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04",
    # docker_args=f"-e CLEARML_AGENT_GIT_USER=oauth2 -e CLEARML_AGENT_GIT_PASS={token}",
)

Task.enqueue(my_task, "default")
