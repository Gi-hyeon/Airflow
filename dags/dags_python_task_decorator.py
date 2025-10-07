import pendulum

from airflow.sdk import DAG, task

with DAG(
    dag_id="dags_python_task_decorator",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["example"],
) as dag:
    # [START howto_operator_python]
    @task(task_id="python_task_1")
    def print_context(some_input):
       print(f'{some_input}')

    python_task_1 = print_context("task_decorator execute")     # task 객체가 필요없음
    # [END howto_operator_python]