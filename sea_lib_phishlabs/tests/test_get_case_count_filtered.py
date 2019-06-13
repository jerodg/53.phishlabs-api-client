#!/usr/bin/env python3.7
"""Phishlabs API: Test Get Case Count Filtered
    Jerod Gawne, 2019.06.13 <https://github.com/jerodg>"""
import time

import pytest
from sea_lib_base.base_utils import bprint

from sea_lib_phishlabs.phishlabs_api import PhishlabsApi


@pytest.mark.asyncio
async def test_get_case_count_filtered():
    ts = time.perf_counter()
    bprint('Test: Get Case Count Filtered')

    with PhishlabsApi(sem=10) as plapi:
        results = await plapi.get_case_count()
        # print('\nresults:', results)  # debug
        filtered_results = await plapi.get_case_count(case_status='Assigned')
        # print('\nresults:', results)  # debug

        assert type(results) is int
        assert type(filtered_results) is int

        print(f'Found {results} cases.')
        print(f'Found {filtered_results} filtered cases.')

    bprint(f'-> Completed in {round((time.perf_counter() - ts) / 60, 2)} minutes.')
