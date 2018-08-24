#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AI application to predict your age
"""

from random import randint


def predict_age():
    """ Predicts one's age based on random number between 1 and 99

     Args:
        None

    Returns:
        age: int between 1 and 99
    """
    return randint(1,99)
