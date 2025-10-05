import datetime

import pendulum

from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.sdk import DAG

    
with DAG(
    # dag_id="example_bash_operator", # dags id = python file name 직관적으로 빨리 찾을 수 있게 일치시킴
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), # UTC -> Asia/Seoul UTC 설정 시 9시간 차이
    catchup=False
    # catchup=False,  # 03/01 일자에 돌릴 시 앞에 누락된 날짜도 같이 돌릴 것이냐 -> 일반적 false
    # dagrun_timeout=datetime.timedelta(minutes=60),    # max timeout 이라고 생각하면 됨
    # tags=["example", "example2"], # tags 들의 옵션들임 -> option이니 지워도 무방
    # params={"example_key": "example_value"},  # tasks에 공통적으로 넘겨줄 파라미터가 있다면, 여기에 지정 => 3.1.0 예시에는 없었음
) as dag:
    # run_this = BashOperator(  tash의 객체 명이 됨
    bash_t1 = BashOperator(
        # task_id="run_after_loop", # task의 작업도 객체명과 동일하게 해주어야 찾기 쉬움
        # bash_command="echo https://airflow.apache.org/",
        task_id="bash_t1",
        bash_command="echo whoami",
    )
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2