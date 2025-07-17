from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
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
    dag_id="weather-api-dbt-orchestrator",
    default_args=default_args,
    schedule=timedelta(minutes=1),
)

with dag:
    #tash 1
    task1 = PythonOperator(
        task_id="insert-data-task",
        python_callable=main,
    )

    task2 = DockerOperator(
        task_id="transform-data-task",
        image="ghcr.io/dbt-labs/dbt-postgres:1.9.latest",
        command="run",
        working_dir="/usr/app/",
        mounts=[
            Mount(
                source="//home/toan/PycharmProjects/Weather-RealTime-Pipeline/dbt/my_project",
                target="/usr/app/",
                type="bind",
            ),
            Mount(
                source="/home/toan/PycharmProjects/Weather-RealTime-Pipeline/dbt/profiles.yml",
                target="/root/.dbt/profiles.yml",
                type="bind",
            )
        ],
        network_mode="weather-realtime-pipeline_my-network",
        docker_url="unix://var/run/docker.sock",
        auto_remove="success",
    )

    task1 >> task2