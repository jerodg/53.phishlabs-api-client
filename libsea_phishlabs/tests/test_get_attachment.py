#!/usr/bin/env python3.7
"""Test Phishlabs API- Get Attachment: Jerod Gawne, 2019.01.09 <https://github.com/jerodg/>"""
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
    def test_get_attachment():
        assert plapi.CACHE['random_attachment'] is not None
        attachment_id = plapi.CACHE['random_attachment']

        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(plapi.get_attachment(attachment_id=attachment_id))
        # print('\nresults: ', results)

        assert type(results) is dict
        assert results['success'] is not None
        assert results['failure'][0] is None

        print(format_banner(f'Test: Get Attachment {attachment_id}'))
        print('Success Result:')
        print(*results['success'][:5], sep='\n')
        print('\nFailure Result:')
        print(*results['failure'][:5], sep='\n')


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))
