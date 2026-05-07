from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from detect_anomalies import detect_anomalies
from visualize_anomalies import plot_anomalies


default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
}


with DAG(
    dag_id="anomaly_detection_pipeline",
    default_args=default_args,
    schedule_interval=None,
    catchup=False
) as dag:

    detect_task = PythonOperator(
        task_id="detect_anomalies",
        python_callable=detect_anomalies
    )

    visualize_task = PythonOperator(
        task_id="visualize_anomalies",
        python_callable=plot_anomalies
    )

    detect_task >> visualize_task