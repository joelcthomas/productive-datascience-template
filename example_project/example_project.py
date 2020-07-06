# %%
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

from raw_data import raw_data
from summary import summary
import select_data

# %%
if __name__ == '__main__':
    raw_data = raw_data(spark)

    filtered_data = select_data.select_data_between_days(raw_data, '2020-04-01', '2020-04-30')
    print(summary(filtered_data))
