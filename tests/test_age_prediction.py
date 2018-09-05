#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unit test cases for predicting age
"""

from futurepredictor import age_predictor


def test_predicted_age_is_numeric():
    assert type(age_predictor.predict_age()) is int

def test_predicted_age_is_between_1_99():
    predicted_age = age_predictor.predict_age()
    assert predicted_age>=1 & predicted_age<=99
