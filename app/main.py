from moose_lib import Task, TaskConfig, TaskContext, Workflow, WorkflowConfig
from pydantic import BaseModel
 
class Foo(BaseModel):
  name: str;
 
def run_task1(ctx: TaskContext[Foo]) -> None:
  name = ctx.input.name or "world"
  greeting = f"hello, {name}!"
 
task1 = Task[Foo, None](
  name="task1",
  config=TaskConfig(run=run_task1)
)
 
myworkflow = Workflow(
  name="myworkflow",
  config=WorkflowConfig(starting_task=task1)
)
