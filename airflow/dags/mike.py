from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

from utilities import airflow_utils

DP_NAME = 'TEST'

with DAG(
        dag_id='test_edr_report',
        schedule=None,
        start_date=datetime(2024, 1, 1),
        default_args=airflow_utils.default_args,
        tags=['RGM', airflow_utils.workspace_name.upper()],
        catchup=False,
        on_failure_callback=airflow_utils.custom_failure_function,
        on_success_callback=airflow_utils.custom_success_function,
        doc_md=__doc__
) as dag:
    t_start = EmptyOperator(task_id='start')
    t_end = EmptyOperator(task_id='end')

    trigger_elementary_workflow_numerator_data_product_task = PythonOperator(
            task_id='trigger_github_workflow_task',
            python_callable=airflow_utils.trigger_github_workflow,
            provide_context=True,
            op_kwargs={
                    'dp_name': DP_NAME,
                    'elem_env': airflow_utils.env
            })

    check_status_elementary_workflow_data_product = PythonOperator(
            task_id='check_workflow_status_task',
            python_callable=airflow_utils.check_edr_workflow_status,
            provide_context=True,
    )

    (
            t_start >>
            trigger_elementary_workflow_numerator_data_product_task >>
            check_status_elementary_workflow_data_product >>
            t_end
    )
