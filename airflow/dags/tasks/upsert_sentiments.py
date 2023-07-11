from datetime import datetime

from airflow.operators.python_operator import PythonOperator

from airflow import DAG


def get_python_version():
    import sys
    print(f"Python Version: {sys.version}")

dag = DAG(
    'get_python_version',
    description='DAG to retrieve Python version',
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False
)

task_get_python_version = PythonOperator(
    task_id='get_python_version',
    python_callable=get_python_version,
    dag=dag
)
