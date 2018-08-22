#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AI application to predict the future
"""

import sys
import argparse
from wealth_predictor import wealth_predictor
from age_predictor import age_predictor

def parse_args(argv=None):
    parser = argparse.ArgumentParser(description='Future Predictor - It predicts your life!')
    parser.add_argument('-t', '--type', required=True,
                        choices=['none', 'age', 'wealth'],
                        default='none',
                        help='What would you like to predict?')

    return parser.parse_args(argv)


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    if args.type == 'none':
        print('You have selected to predict nothing')
    elif args.type == 'age':
        print(age_predictor.predict_age())
    elif args.type == 'wealth':
        print(wealth_predictor.predict_wealth())
    else:
        print('I can\'t predict them yet')