# -*- coding: utf-8 -*-
"""
Unit test cases for data access
"""

from covid_county import raw_data

from pyspark.sql import SparkSession, dataframe 
spark = SparkSession.builder.getOrCreate()


def test_raw_data_type():
    assert isinstance(raw_data(spark), dataframe.DataFrame)
