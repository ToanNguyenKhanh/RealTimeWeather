from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

sys.path.append('/opt/airflow/api-request')
from insert_records import main

default_args = {
    'description': 'Orchestrator',
    'start_date': datetime(2025, 7, 16),
    'catchup': False,
}

dag = DAG(
    dag_id="weather-api-orchestrator",
    default_args=default_args,
    schedule=timedelta(minutes=5),
)

with dag:
    #tash 1
    task1 = PythonOperator(
        task_id="insert-data-task",
        python_callable=main,
    )