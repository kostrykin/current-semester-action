#!/usr/bin/env python

import argparse
import pathlib
import os
from datetime import date, timedelta
from typing import Literal


def expand(today: date, floor: Literal['', 'ws', 'ss'], which: Literal['current', 'next']):
    assert floor in ('', 'ws', 'ss')
    assert which in ('current', 'next')

    year = today.year % 2000
    if which == 'next':
        year += 1

    if 4 <= today.month <= 9:
        prefix = 'ss'
    else:
        prefix = 'ws'
        if today.month < 4:
            year -= 1

    if any((floor == 'ws' and prefix == 'ss', floor == 'ss' and prefix == 'ws')):
        return expand(today - timedelta(days=6 * 30), floor='', which=which)

    else:
        name = f'{prefix}{year}'
        description = f'{prefix.upper()} {year}' + (f'/{year + 1}' if prefix == 'ws' else '')

        return {
            'name': name,
            'description': description,
        }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--floor', type=str, default='')
    parser.add_argument('--which', type=str, default='current')
    args = parser.parse_args()

    today = date.today()
    data = expand(today, floor=args.floor, which=args.which)
    for key, value in data.items():
        print(f'{key}={value}')