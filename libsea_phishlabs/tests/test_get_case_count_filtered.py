#!/usr/bin/env python3.7
"""Test Phishlabs API- Get Case Count Filtered: Jerod Gawne, 2019.01.09 <https://github.com/jerodg/>"""
import asyncio
import logging
import sys
import traceback

import pytest
from jgutils.persistentdict import PersistentDict as PerDi
from os.path import (abspath, dirname, realpath)
from random import choice

from libsea_phishlabs.phishlabs_api import PhishlabsApi

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)
ROOT = dirname(abspath(__file__))


def format_banner(message) -> str:
    msg_len = len(message)
    if msg_len >= 80:
        return message

    ast = (80 - msg_len) // 2
    ast = '*' * ast
    msg = f'\n{ast}{message}{ast}\n'

    return msg


with PhishlabsApi(root=ROOT, sem=10) as plapi:
    def test_get_case_count_filtered():
        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(plapi.get_case_count(case_status='Assigned'))
        # print('\nresults: ', results)  # debug

        assert type(results) is int

        print(format_banner(f'Test: Get Case Count Filtered'))
        print(f'\tTotal Filtered Cases: {results}')


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))
