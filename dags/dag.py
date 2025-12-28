from airflow.sdk import dag, task
from airflow.operators.bash import BashOperator
from datetime import datetime

@dag(dag_id='taskflow_version', start_date=datetime(2021, 1, 1), catchup=False, schedule=None)
def pipeline():

    convert_to_py = BashOperator(
        task_id='convert_to_py',
        bash_command='docker exec spark_container jupyter nbconvert --to python /opt/spark/work-dir/*.ipynb',
    )


    etl1 = BashOperator(
        task_id='etl1',
        bash_command='docker exec spark_container spark-submit /opt/spark/work-dir/ETL1.py',
    )


    etl2 = BashOperator(
        task_id='etl2',
        bash_command='docker exec spark_container spark-submit /opt/spark/work-dir/ETL2.py',
    )


    sampling = BashOperator(
        task_id='sampling',
        bash_command='docker exec spark_container spark-submit /opt/spark/work-dir/sampling-to-csv.py',
    )


    ml = BashOperator(
        task_id='ml',
        bash_command='docker exec spark_container spark-submit /opt/spark/work-dir/ml.py',
    )

    convert_to_py >> etl1 >> etl2 >> sampling >> ml

pipeline()