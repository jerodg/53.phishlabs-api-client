#!/usr/bin/env python3.7
"""Phishlabs API: Test Get Case
    Jerod Gawne, 2019.06.13 <https://github.com/jerodg>"""
import time

import pytest
from sea_lib_base.base_utils import bprint

from sea_lib_phishlabs.phishlabs_api import PhishlabsApi


# todo: auto-grab a case_id


@pytest.mark.asyncio
async def test_get_case():
    ts = time.perf_counter()
    bprint('Test: Get Case')

    with PhishlabsApi(sem=10) as plapi:
        results = await plapi.get_case(case_id='d75359a0-7749-11e9-94e8-0ee0a3f3cb1c')
        # print('\nresults:', results)  # debug

        assert type(results) is dict
        assert results['success'] is not None
        assert results['failure'][0] is None

        print('\nTop 5 Success Result:')
        print(*results['success'][:5], sep='\n')
        print('\nTop 5 Failure Result:')
        print(*results['failure'][:5], sep='\n')

    bprint(f'-> Completed in {round((time.perf_counter() - ts) / 60, 2)} minutes.')
