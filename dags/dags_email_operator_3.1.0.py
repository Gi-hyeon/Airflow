import datetime

import pendulum

from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.smtp.operators.smtp import EmailOperator
from airflow.sdk import DAG

with DAG(
    dag_id="dags_email_operator_3.1.0",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    send_email_task = EmailOperator(
        task_id='send_email_task',
        conn_id='conn_smtp_gmail',      #airflow 3.1.0 이후부터 connection 정보 추가
        to='hmms52@naver.com',
        subject='Airflow SUCESS MAIL',
        html_content='Airflow Workflow SUCESS'
    )