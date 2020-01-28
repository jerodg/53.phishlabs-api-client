#!/usr/bin/env python3.7
"""Phishlabs API: Test Get Case Count
    Jerod Gawne, 2019.01.09 <https://github.com/jerodg>"""
import time

import pytest
from sea_lib_base.base_utils import bprint

from phishlabs_api_client.phishlabs_api import PhishlabsApi


@pytest.mark.asyncio
async def test_get_case_count():
    ts = time.perf_counter()
    bprint('Test: Get Case Count')

    with PhishlabsApi(sem=10) as plapi:
        results = await plapi.get_case_count()
        # print('\nresults:', results)  # debug

        assert type(results) is int

        print(f'Found {results} cases.')

    bprint(f'-> Completed in {round((time.perf_counter() - ts) / 60, 2)} minutes.')
