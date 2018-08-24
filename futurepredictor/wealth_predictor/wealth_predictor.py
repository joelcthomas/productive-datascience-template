#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AI application to predict your wealth
"""

from random import randint


def predict_wealth():
    """ Predicts one's wealth in millions based on random number between 10 and 999
    
    Args:
        None

    Returns:
        wealth: int between 10 and 999
    """
    return randint(10,999)
