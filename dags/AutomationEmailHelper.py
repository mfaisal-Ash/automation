from datetime import datetime 
from airflow.models import DAG,Variable
from airflow.operators.python_operator import PythonOperator
from bots.EmailHelper import send


default_args = {
    'owner': 'sidiq2',
    # 'depends_on_past': False,
    'start_date': datetime(2024, 11, 14),
    # 'email_on_failure': False,
    # 'email_on_retry': False,
    # 'retries': 1,
    # 'retry_delay': timedelta(minutes=5),
}


with DAG(
    dag_id='AutomationEmailHelper',
    default_args=default_args,
    schedule_interval=None) as dag:

    send_email=PythonOperator(
        task_id='send_email',
        python_callable=send,
        dag=dag
    )

    send_email
