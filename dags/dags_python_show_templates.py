import datetime
import pendulum

from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.sdk import DAG, task

with DAG(
    dag_id="dags_python_show_templates",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2025, 9, 20, tz="Asia/Seoul"),
    catchup=True    # True => 2025/09/20 ~ 2025/10/08 전부 수행 진행
) as dag:
    
    @task(task_id='python_task')
    def show_templates(**kwargs):
        from pprint import pprint 
        pprint(kwargs)  # 정렬 print문 => list, dict 등

    show_templates()