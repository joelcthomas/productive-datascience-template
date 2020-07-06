
def raw_data(spark):
    return spark.read.format("csv").option("header", "true").load("/mnt/joel/covid-us-county")