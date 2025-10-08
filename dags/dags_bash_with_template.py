import datetime
import pendulum

from airflow.providers.standard.operators.bash import BashOperator
# from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.sdk import DAG

with DAG(
    dag_id="dags_bash_with_template",
    schedule="10 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    bash_t1 = BashOperator(
        task_id='bash_t1',
        bash_command='echo "data_interval_end: {{ data_interval_end }}"'
    )

    # Airflow 3.0~ 버전부터는 data_interval_start = data_interval_end 값이 동일하게 나옴 => 참고
    bash_t2 = BashOperator(
        task_id='bash_t2',
        env={
            'START_DATE':'{{data_interval_start | ds}}',
            'END_DATE':'{{data_interval_end | ds}}'
        },
        bash_command='echo $START_DATE && echo $END_DATE'
    )

    bash_t1 >> bash_t2