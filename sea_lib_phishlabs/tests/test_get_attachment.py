#!/usr/bin/env python3.7
"""Test Phishlabs API: Get Attachment
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


# todo: auto-grab an attachment id

@pytest.mark.asyncio
async def test_get_attachment():
    ts = time.perf_counter()
    bprint('Test: Get Attachment')

    with PhishlabsApi(root=ROOT, sem=10) as plapi:
        results = await plapi.get_attachments(attachments={'id': '1f5d2f83-700a-11e9-b826-0eb92493f786'})
        # print('\nresults:', results)  # debug

        assert type(results) is dict
        assert results['success'] is not None
        assert results['failure'][0] is None

        print('\nTop 5 Success Result:')
        print(*results['success'][:5], sep='\n')
        print('\nTop 5 Failure Result:')
        print(*results['failure'][:5], sep='\n')

    bprint(f'-> Completed in {round((time.perf_counter() - ts) / 60, 2)} minutes.')


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))
