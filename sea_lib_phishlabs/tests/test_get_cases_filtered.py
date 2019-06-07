#!/usr/bin/env python3.7
"""Test Phishlabs API- Get Cases Filtered: Jerod Gawne, 2019.01.09 <https://github.com/jerodg/>"""
import asyncio
import logging
import sys
import traceback

import pytest
from jgutils.persistentdict import PersistentDict as PerDi
from os.path import (abspath, dirname, realpath)
from random import choice

from sea_lib_phishlabs.phishlabs_api import PhishlabsApi

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
    def test_get_cases_filtered():
        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(plapi.get_cases(case_status='Assigned'))
        # print('\nresults: ', results)  # debug

        assert type(results) is dict
        assert results['success'] is not None
        assert results['failure'][0] is None
        # print('len_results: ', len(results['success']))

        print(format_banner(f'Test: Get Cases Filtered {plapi.case_count}'))
        print('Top 5 Success Result:')
        print(*results['success'][:5], sep='\n')
        print('\nTop 5 Failure Result:')
        print(*results['failure'][:5], sep='\n')


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))
