#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AI application to predict the future
"""

import sys
import argparse
from wealth_predictor import wealth_predictor
from age_predictor import age_predictor
from predictor_utils import config_reader


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description='Future Predictor - It predicts your life!')
    parser.add_argument('-t', '--type', required=True,
                        choices=['none', 'age', 'wealth'],
                        default='none',
                        help='What would you like to predict?')

    return parser.parse_args(argv)


if __name__ == '__main__':
    # Reading arguments
    args = parse_args(sys.argv[1:])

    # Reading Config
    config = config_reader.read_config()
    print("Seed:"+config['future_predictor']['seed'])

    # Process future predictor
    if args.type == 'none':
        print('You have selected to predict nothing')
    elif args.type == 'age':
        print("You are "+str(age_predictor.predict_age())+" years old!")
    elif args.type == 'wealth':
        print("You are worth "+str(wealth_predictor.predict_wealth())+" Million $$$")
    else:
        print('I can\'t predict them yet')
