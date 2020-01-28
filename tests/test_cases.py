#!/usr/bin/env python3.8
"""Phishlabs API Client: Test Cases
Copyright © 2019 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""
import time

import pytest
from os import getenv

from base_api_client import bprint, Results, tprint
from phishlabs_api_client import PhishlabsApiClient
from phishlabs_api_client.models import Query


@pytest.mark.asyncio
async def test_get_case_count():
    ts = time.perf_counter()
    bprint('Test: Get Case Count')

    async with PhishlabsApiClient(cfg=f'{getenv("CFG_HOME")}/phishlabs_api_client.toml') as plac:
        results = await plac.get_case_count()
        # print(results)

        assert type(results) is Results
        assert len(results.success) == 1
        assert not results.failure

        tprint(results)  # Should return all cases

    bprint(f'-> Completed in {(time.perf_counter() - ts):f} seconds.')


@pytest.mark.asyncio
async def test_get_cases_count_filtered():
    ts = time.perf_counter()
    bprint('Test: Get Cases Count Filtered')

    async with PhishlabsApiClient(cfg=f'{getenv("CFG_HOME")}/phishlabs_api_client.toml') as plac:
        results = await plac.get_case_count(query=Query(caseType=['Phishing']))
        # print(results)

        assert type(results) is Results
        assert len(results.success) == 1
        assert not results.failure

        tprint(results)  # Should return all cases across all cases

    bprint(f'-> Completed in {(time.perf_counter() - ts):f} seconds.')


@pytest.mark.asyncio
async def test_get_all_cases():
    ts = time.perf_counter()
    bprint('Test: Get All Cases')

    async with PhishlabsApiClient(cfg=f'{getenv("CFG_HOME")}/phishlabs_api_client.toml') as plac:
        results = await plac.get_case_count()
        count = results.success[0]['header']['totalResult']

        results = await plac.get_cases()
        # print(results)

        assert type(results) is Results
        assert len(results.success) == count
        assert not results.failure

        tprint(results, top=5)

    bprint(f'-> Completed in {(time.perf_counter() - ts):f} seconds.')


@pytest.mark.asyncio
async def test_get_all_cases_filtered():
    ts = time.perf_counter()
    bprint('Test: Get All Cases Filtered')

    async with PhishlabsApiClient(cfg=f'{getenv("CFG_HOME")}/phishlabs_api_client.toml') as plac:
        results = await plac.get_case_count(query=Query(caseType=['Phishing']))
        count = results.success[0]['header']['totalResult']

        results = await plac.get_cases(query=Query(caseType=['Phishing']))
        # print(results)

        assert type(results) is Results
        assert len(results.success) == count
        assert not results.failure

        tprint(results, top=5)

    bprint(f'-> Completed in {(time.perf_counter() - ts):f} seconds.')


@pytest.mark.asyncio
async def test_get_one_case():
    ts = time.perf_counter()
    bprint('Test: Get One Container')

    async with PhishlabsApiClient(cfg=f'{getenv("CFG_HOME")}/phishlabs_api_client.toml') as plac:
        results = await plac.get_cases(case_id='<insert_case-id_here>')
        # print(results)

        assert type(results) is Results
        assert len(results.success) == 1
        assert not results.failure

        tprint(results)

    bprint(f'-> Completed in {(time.perf_counter() - ts):f} seconds.')
