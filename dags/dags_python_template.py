import datetime
import pendulum

# from airflow.providers.standard.operators.bash import BashOperator
# from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG, task

with DAG(
    dag_id="dags_python_template",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2023, 3, 10, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    def python_function1(start_date, end_date, **kwargs):
        print(start_date)
        print(end_date)
    # op_kwargs <- jinja 템플릿 변수를 직접 넣어서 사용하는 방식
    python_t1 = PythonOperator(
        task_id='python_t1',
        python_callable=python_function1,
        op_kwargs={'start_date':'{{data_interval_start | ds}}', 'end_date':'{{data_interval_end | ds}}'}
    )


    # kwargs <- 사용할 수 있는 템플릿 변수가 정의되어 있기 때문에 꺼내서 사용하는 방식
    @task(task_id='python_t2')
    def python_function2(**kwargs):
        print(kwargs)
        print('ds:' + kwargs['ds'])
        print('ts:' + kwargs['ts'])
        print('data_interval_start:' + str(kwargs['data_interval_start']))
        print('data_interval_end:' + str(kwargs['data_interval_end']))
        print('task_instance:' + str(kwargs['ti']))


    python_t1 >> python_function2()