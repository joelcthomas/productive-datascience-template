# -*- coding: utf-8 -*-
"""
Unit test cases for Data Summary
"""

from covid_county import raw_data
from covid_county import summary
import pandas as pd

from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()


def test_summary_data_type():
    assert isinstance(summary(raw_data(spark)), pd.core.frame.DataFrame)
