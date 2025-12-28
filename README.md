# Celestial object classification pipeline
This project is a demonstration of an end to end pipeline orchestrated using Apache Airflow that reads data from a csv file downloaded from SDSS(Sloan Digital Sky Survey) using SQL, cleans the data using Apache Spark's python wrapper pyspark, loads
it to a PostgreSQL database and runs a sample of data through xgboost algorithm to classify the entries into one of the three categories - star, galaxy, quasar. All of this is done in Docker using docker-compose inorder
to keep my laptop clean and the project reproducible :)

## Dataset
The data set contains the intensity of light that is captured by the SDSS telescope in 5 different wavelength bands namely u-ultraviolet, g-green, r-red, i-near infrared, z-infrared and along with these the data also 
contains the measured redshift and the category to which this object belongs to. Inorder to accurately predict the category of the object we first need to do a little feature engineering, the absolute values of the
intensities are not that helpfull, we need their differences because this is what gives the observed color for eg. if intensity of red is high but green is low then the object is red and is most likely a red giant star
but if the difference is not that high then the object could be a galaxy. This doesnt depend on the absolute values hence first we use pyspark to calculate and record the differences in PosgreSQL database. Apache spark
is needed for this because the dataset contains almost a million rows and it wont fit into the RAM of my laptop. Pyspark handles large data very well due to its distributed computing nature, the entire data need not
exist on the RAM for pyspark operations to work. The dataset is too large to upload to github hence is not present in this repo, it must be put in the 'notebooks' directory with the label raw_data.csv. This directory
needs to be mounted in spark docker container on the path /opt/spark/work-dir.

## Spark and Airflow
The 'spark' directory contains the dockerfile that builds spark image and it also contains 'jars' directory that must be mounted on /opt/spark/jars. This is needed to communicate with postgreSQL database.
The dockerfile in the root directory is Airflow's dockerfile. The root directory also contains docker-compose.yml which has 3 services namely - spark, airflow, postgresql. The 'dags' folder must contain the dag
that airflow needs to run, this must also be mounted onto airflow's /opt/airflow/dags folder. Similarly the 'logs' folder also needs to mounted to /opt/airflow/logs.

## How to run?
After adding all the required dependencies and data to the correct folders, simply typing docker-compose build followed by docker-compose up should get the containers working. Spark can be accessed at localhost:8888
and airflow can be accessed at 8080. Find the dag in airflow's GUI and trigger it. All the tasks within the dag will run successfully and the classification report and best parameters will be printed to results.txt file inside
the 'notebooks' directory along with .png of confusion matrix.

## Results
- precision 0.98
- recall 0.98
- f1-score 0.98
- QSO recall - 0.99 (important object, high recall was the criteria used in grid search optimisation)
- best learning rate 0.05
- best max depth 8








  
