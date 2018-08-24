#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Read config for futurepredictor
"""

import os
import configparser


def read_config():
    """Reads config file from config directory

    Args:
        None

    Returns:
        config
    """
    config = configparser.ConfigParser()
    config_file = os.path.join(os.path.dirname(__file__), '../../config/config.ini')
    config.read(config_file)

    return config