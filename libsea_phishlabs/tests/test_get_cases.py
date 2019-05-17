#!/usr/bin/env python3.7
"""Test Phishlabs API: Get Cases
   Jerod Gawne, 2019.01.09 <https://github.com/jerodg/>"""
import logging
import sys
import time
import traceback
from os.path import abspath, dirname, realpath

import pytest

from libsea_base.base_api_utils import bprint
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
      def test_get_cases():
        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(plapi.get_cases())
        # print('\nresults: ', results)  # debug

        assert type(results) is dict
        assert results['success'] is not None
        assert results['failure'][0] is None

        # Grab a random case with an attachment
        while 1:
            try:
                rcid = choice(results['success'])
                if len(rcid['attachments']) >= 1:
                    plapi.CACHE['random_case'] = rcid['caseId']
                    print('random_case: ', plapi.CACHE['random_case'])  # debug
                    break
            except KeyError:
                pass

        print(format_banner(f'Test: Get Cases {plapi.case_count}'))
        print('Top 5 Success Result:')
        print(*results['success'][:5], sep='\n')
        print('\nTop 5 Failure Result:')
        print(*results['failure'][:5], sep='\n')


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))
