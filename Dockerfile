FROM apache/airflow:3.1.5-python3.13

#volume mount
# docker run -it --user root -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock -v ./dags:/opt/airflow/dags -v ./logs:/opt/airflow/logs airflow-image airflow standalone