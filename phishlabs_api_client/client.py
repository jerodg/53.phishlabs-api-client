#!/usr/bin/env python3.8
"""Phishlabs API Client
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

import asyncio
import logging
from typing import Any, List, NoReturn, Optional, Tuple, Union
from uuid import uuid4
from phishlabs_api_client.models import Query

from base_api_client import BaseApiClient, Results
logger = logging.getLogger(__name__)

# todo: need to write performance test to determine best SEM/page_size ratio


class PhishlabsApiClient(BaseApiClient):
    SEM: int = 15

    def __init__(self, cfg: Union[str, dict], sem: Optional[int] = None):
        BaseApiClient.__init__(self, cfg=cfg, sem=sem or self.SEM)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await BaseApiClient.__aexit__(self, exc_type, exc_val, exc_tb)

    async def get_case_count(self, query: Optional[Query] = Query(maxRecords=1, offset=0)) -> Results:
        """
        Performs a single page query to get the 'totalResult' based on specified Query.
        Args:
            query (Optional[Query]):

        Returns:
            results (Results)
        """
        # todo: need to see actual output to verify this
        logger.debug('Getting case count...')

        tasks = [asyncio.create_task(self.request(method='get',
                                                  end_point='/cases',
                                                  request_id=uuid4().hex,
                                                  params=query.params()))]

        results = Results(data=await asyncio.gather(*tasks))

        logger.debug('-> Complete.')

        return await self.process_results(results)

    async def get_cases(self, case_id: Optional[str], query: Optional[Query] = Query()) -> Results:
        """
        Can retrieve:
            - All cases
            - A single case
        Args:
            case_id (Optional[int]):
            query (Optional[Query]):

        Returns:
            results (Results)
        """
        if case_id:
            ep = f'/cases/{case_id}'
        else:
            ep = '/cases'

        if not case_id:
            # todo: rewrite for phishlabs
            # page_limit = (await self.get_case_count(query=query)).success[0]['num_pages']
            page_limit = 0
        else:  # When we're getting a single container we can skip paging
            page_limit = 1

        logger.debug('Getting cases(s)...')

        tasks = [asyncio.create_task(self.request(method='get',
                                                  end_point=ep,
                                                  request_id=uuid4().hex,
                                                  params=query.params(offset=i)))
                 for i in range(0, page_limit, query.maxRecords)]

        results = Results(data=await asyncio.gather(*tasks))

        logger.debug('-> Complete.')

        return await self.process_results(results, 'data')

    async def get_attachments(self, attachment_id: Optional[str], case_id: Optional[str]):
        if case_id:
            pass

        logger.debug('Getting attachment(s)...')

        logger.debug('-> Complete.')


if __name__ == '__main__':
    print(__doc__)
