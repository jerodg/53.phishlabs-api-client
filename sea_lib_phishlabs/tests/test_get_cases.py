#!/usr/bin/env python3.7
"""Phishlabs API: Test Get Cases
    Jerod Gawne, 2019.06.13 <https://github.com/jerodg>"""
import time

import pytest
from os.path import realpath
from sea_lib_base.base_utils import bprint

from sea_lib_phishlabs.phishlabs_api import PhishlabsApi


@pytest.mark.asyncio
async def test_get_cases():
    ts = time.perf_counter()
    bprint('Test: Get Cases')

    with PhishlabsApi(sem=10) as plapi:
        results = await plapi.get_cases()
        # print('\nresults: ', results)  # debug

        assert type(results) is dict
        assert results['success'] is not None
        assert results['failure'][0] is None

        print(f'Found {len(results["success"])} cases.')
        print('\nTop 5 Success Result:')
        print(*results['success'][:5], sep='\n')
        print('\nTop 5 Failure Result:')
        print(*results['failure'][:5], sep='\n')
        # print('\nLast 100 Success Result:')
        # print(*results['success'][-100:], sep='\n')
        r2 = set()
        print('len_results:', len(results['success']))
        for r in results['success']:
            print(r['caseId'])
            r2.add(r['caseId'])

        print('r2_len:', len(r2))
        with open(realpath('./data/test_get_cases_success_result.txt'), mode='w+') as of:
            for i, x in enumerate(results['success']):
                of.write(f'{x}\n')
                # print(i, x)

    bprint(f'-> Completed in {round((time.perf_counter() - ts) / 60, 2)} minutes.')
