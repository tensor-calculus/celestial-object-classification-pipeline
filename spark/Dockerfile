FROM apache/spark-py:latest

USER root

ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin
ENV PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9.7-src.zip

COPY /jars /opt/spark/jars

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install jupyterlab scikit-learn pandas seaborn xgboost

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

# docker run --name spark_container -it -p 8888:8888 -v ./notebooks:/opt/spark/work-dir custom-pyspark
# docker run --name postgres_container -p 5432:5432  -e POSTGRES_PASSWORD=password  postgres:18.1