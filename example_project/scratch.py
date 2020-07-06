#%%
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

data = spark.read.format("csv").option("header", "true").load("/mnt/joel/covid-us-county")
data.limit(10).toPandas()

#%%
summary = data.describe().toPandas().set_index("summary").transpose()
print(summary)

# %%
def summary(data):
    return data.describe().toPandas().set_index("summary").transpose()

#%%
print(summary(data))

# %%
