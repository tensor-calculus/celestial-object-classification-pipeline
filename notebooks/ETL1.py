#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .config("spark.jars", "/opt/spark/postgresql-42.7.8.jar") \
    .getOrCreate()


# In[2]:


schema_ddl = "u DOUBLE, g DOUBLE, r DOUBLE, i DOUBLE, z DOUBLE, redshift DOUBLE, class STRING"
df = spark.read.csv("raw_data1.csv", header=True, schema=schema_ddl)
df.show(5)


# In[3]:


df = df.select("u", "g", "r", "i", "z", "class", "redshift")
df.show(5)


# In[4]:


df.printSchema()


# In[5]:


df.dropna(subset=df.columns).count()


# In[6]:


df.distinct().count()


# In[7]:


df.select(['u', 'g', 'r', 'i', 'z', 'redshift', 'class'])


# In[8]:


df.groupBy("class").count().show()


# In[9]:


df.show(5)


# In[14]:


from pyspark.sql.functions import format_number
df = df.withColumn("u-g", format_number(df["u"]-df["g"], 4).cast("double"))
df = df.withColumn("g-r", format_number(df["g"]-df["r"], 4).cast("double"))
df = df.withColumn("r-i", format_number(df["r"]-df["i"], 4).cast("double"))
df = df.withColumn("i-z", format_number(df["i"]-df["z"], 4).cast("double"))


# In[15]:


df = df.select('u', 'g', 'r', 'i', 'z', 'u-g', 'g-r', 'r-i', 'i-z', 'redshift', 'class')


# In[16]:


df.show(5)


# In[17]:


df.write.jdbc(
    url="jdbc:postgresql://host.docker.internal:5432/postgres",
    table="processed_table",
    mode="overwrite",
    properties={
        "user": "postgres",
        "password": "password",
        "driver": "org.postgresql.Driver"
    }
)


# In[ ]:




