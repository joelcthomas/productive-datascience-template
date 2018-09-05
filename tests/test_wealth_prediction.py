#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unit test cases for predicting wealth
"""

from futurepredictor import wealth_predictor


def test_predicted_wealth_is_numeric():
    assert type(wealth_predictor.predict_wealth()) is int

def test_predicted_wealth_is_between_10_999():
    predicted_wealth = wealth_predictor.predict_wealth()
    assert predicted_wealth>10 & predicted_wealth<999
