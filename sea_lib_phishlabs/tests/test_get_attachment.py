#!/usr/bin/env python3.7
"""Phishlabs API: Test Get Attachment
    Jerod Gawne, 2019.06.13 <https://github.com/jerodg>"""
import time

import pytest
from sea_lib_base.base_utils import bprint

from sea_lib_phishlabs.phishlabs_api import PhishlabsApi


# todo: auto-grab an attachment id


@pytest.mark.asyncio
async def test_get_attachment():
    ts = time.perf_counter()
    bprint('Test: Get Attachment')

    with PhishlabsApi(sem=10) as plapi:
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
