#!/usr/bin/env python3.7
"""Phishlabs API: Test Get Cases Filtered 2
   Jerod Gawne, 2019.01.09 <https://github.com/jerodg>"""
import asyncio

from sea_lib_phishlabs.phishlabs_api import PhishlabsApi


def format_banner(message) -> str:
    msg_len = len(message)
    if msg_len >= 80:
        return message

    ast = (80 - msg_len) // 2
    ast = '*' * ast
    msg = f'\n{ast}{message}{ast}\n'

    return msg


with PhishlabsApi(sem=10) as plapi:
    def test_get_cases_filtered2():
        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(plapi.get_cases(case_status=['Closed']))
        # print('\nresults: ', results)  # debug

        assert type(results) is dict
        assert results['success'] is not None
        assert results['failure'][0] is None
        # print('len_results: ', len(results['success']))

        print(format_banner(f'Test: Get Cases Filtered 2 {plapi.get_case_count}'))
        print('Top 5 Success Result:')
        print(*results['success'][:5], sep='\n')
        print('\nTop 5 Failure Result:')
        print(*results['failure'][:5], sep='\n')
