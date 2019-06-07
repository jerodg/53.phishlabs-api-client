#!/usr/bin/env python3.7
"""Test Phishlabs API: Get Case Count
   Jerod Gawne, 2019.01.09 <https://github.com/jerodg/>"""
import logging
import sys
import time
import traceback
from os.path import abspath, dirname

import pytest

from libsea_base.base_api_utils import bprint
from sea_lib_phishlabs.phishlabs_api import PhishlabsApi

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)
ROOT = dirname(abspath(__file__))


@pytest.mark.asyncio
async def test_get_case_count():
    ts = time.perf_counter()
    bprint('Test: Get Case Count')

    with PhishlabsApi(root=ROOT, sem=10) as plapi:
        results = await plapi.get_case_count()
        # print('\nresults:', results)  # debug

        assert type(results) is int

        print(f'Found {results} cases.')

    bprint(f'-> Completed in {round((time.perf_counter() - ts) / 60, 2)} minutes.')


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))