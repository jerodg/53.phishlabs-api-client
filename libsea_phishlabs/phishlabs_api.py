#!/usr/bin/env python3.7
"""Phishlabs API: Jerod Gawne, 2019.01.09 <https://github.com/jerodg>"""
import asyncio
import logging
from sys import exc_info, argv
from traceback import print_exception
from typing import (Any, List, Optional, Tuple, Union)

import aiohttp as aio
from aiohttp import BasicAuth
from os import (getenv)
from os.path import abspath, dirname, realpath, basename
from tenacity import after_log, retry, retry_if_exception_type, wait_random_exponential
from uuid import uuid4

from libsea_base.base_api import ApiBase

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)
RETRY: int = 5


# todo: submit bug report; when autocompleting an overridden function the return type isn't copied over


class PhishlabsApi(ApiBase):
    AUTH: BasicAuth = BasicAuth(login=getenv('PL_USER'), password=getenv('PL_PASS'))
    CHUNK_SIZE: int = 1024
    MAX_RECORDS: int = 100  # API Max is 200, minimum is 20 (default)
    PROXY: str = getenv('PL_PROXY')
    ROOT = dirname(abspath(__file__))
    SEM: int = 10
    URI_BASE = f'{getenv("PL_URI")}/v1/data'
    URI_ATTACHMENT = f'{URI_BASE}/attachment'
    URI_CASE = f'{URI_BASE}/cases'
    URI_OPEN_CASE = f'{URI_CASE}/open'
    URI_CLOSED_CASE_URI = f'{URI_CASE}/closed'
    TRUST_ENV: bool = True  # Reads ~/.netrc or HTTP_PROXY/HTTPS_PROXY Envars for proxy info/credentials
    VERIFY_SSL: bool = False  # Verify SSL Certifcates

    def __init__(self, root: Optional[str] = None, sem: Optional[int] = None, ):
        ApiBase.__init__(self, root=root or self.ROOT, sem=sem or self.SEM, parent=basename(argv[0][:-3]))

    def __exit__(self, exc_type, exc_val, exc_tb):
        ApiBase.__exit__(self, exc_type, exc_val, exc_tb)

    def pl_process_params(self, **kwargs) -> list:
        parms = {'caseStatus': kwargs.pop('case_status', ['New', 'Assigned', 'Closed']),
                 'caseType':   kwargs.pop('case_type', ['Phishing', 'Phishing Redirect', 'Vishing']),
                 'dateBegin':  kwargs.pop('date_begin', None),
                 'dateEnd':    kwargs.pop('date_end', None),
                 'dateField':  kwargs.pop('date_field', 'caseOpen'),
                 'format':     kwargs.pop('format', 'json'),
                 'maxRecords': kwargs.pop('max_records', self.MAX_RECORDS),
                 'offset':     kwargs.pop('offset', 0)}

        params = []
        for k, v in parms.items():
            if type(v) is list:
                for item in v:
                    params.append((k, item))
            elif v is not None:
                params.append((k, v))

        # print('params: ', params)  # debug
        return params

    async def get_case_count(self, **kwargs: Optional) -> int:
        """See process_params() for kwargs"""
        params = self.pl_process_params(**kwargs, max_records=1)

        async with aio.ClientSession(trust_env=self.TRUST_ENV, auth=self.AUTH) as session:
            if NFO:
                logger.info('Getting case count...')

            tasks = [asyncio.create_task(self.__get_case_count(session=session, params=params))]
            results = await asyncio.gather(*tasks)

            if NFO:
                logger.info('\tComplete.')

        await session.close()

        if NFO:
            logger.info(f'\tFound {results["header"]["totalResult"]} cases')

        return (await self.process_results(results))['success'][0]['header']['totalResult']

    @retry(retry=retry_if_exception_type(aio.ClientError),
           wait=wait_random_exponential(max=RETRY),
           after=after_log(logger, logging.WARNING))
    async def __get_case_count(self, session: aio.ClientSession, params: list) -> Union[dict, aio.ClientResponse]:
        async with self.sem:
            response = await session.get(self.URI_CASE, params=params, ssl=self.VERIFY_SSL, proxy=self.PROXY)

            if 200 <= response.status <= 299:
                return await response.json(content_type=None)  # Set content type if known
            elif response.status in [429, 500, 502, 503, 504]:
                raise aio.ClientError
            else:
                return response

    async def get_cases(self, **kwargs: Optional) -> dict:
        """See process_params() for kwargs"""
        params = self.pl_process_params(**kwargs, offset=None)
        case_count = await self.get_case_count(**kwargs)

        async with aio.ClientSession(trust_env=self.TRUST_ENV, auth=self.AUTH) as session:
            if NFO:
                logger.info('Getting cases...')

            tasks = []
            for x in range(0, case_count + 1, self.MAX_RECORDS):
                params.append(('offset', x))
                tasks.append(asyncio.create_task(
                        self.__get_cases(session=session, params=params)))
                del params[-1]

            results = await asyncio.gather(*tasks)

            if NFO:
                logger.info('\tComplete.')

        await session.close()

        return await self.process_results(results, 'data')

    @retry(retry=retry_if_exception_type(aio.ClientError),
           wait=wait_random_exponential(max=RETRY),
           after=after_log(logger, logging.WARNING))
    async def __get_cases(self, session: aio.ClientSession, params: List[Tuple[Any, Any]]) -> Union[
        dict, aio.ClientResponse]:
        async with self.sem:
            response = await session.get(self.URI_CASE, params=params, ssl=self.VERIFY_SSL, proxy=self.PROXY)
            if 200 <= response.status <= 299:
                return await response.json(content_type=None)  # Set content type if known
            elif response.status in [429, 500, 502, 503, 504]:
                raise aio.ClientError
            else:
                return response

    async def get_case(self, case_id: str) -> dict:
        async with aio.ClientSession(trust_env=self.TRUST_ENV, auth=self.AUTH) as session:
            if NFO:
                logger.info(f'Getting case {case_id}...')

            tasks = [asyncio.create_task(self.__get_case(session=session, case_id=case_id))]
            results = await asyncio.gather(*tasks)

            if NFO:
                logger.info('\tComplete.')

        await session.close()

        return await self.process_results(results, 'data')

    @retry(retry=retry_if_exception_type(aio.ClientError),
           wait=wait_random_exponential(max=RETRY),
           after=after_log(logger, logging.WARNING))
    async def __get_case(self, session: aio.ClientSession, case_id: str) -> Union[dict, aio.ClientResponse]:
        async with self.sem:
            response = await session.get(f'{self.URI_CASE}/{case_id}', ssl=self.VERIFY_SSL, proxy=self.PROXY)

            if 200 <= response.status <= 299:
                return await response.json(content_type=None)  # Set content type if known
            elif response.status in [429, 500, 502, 503, 504]:
                raise aio.ClientError
            else:
                return response

    async def get_attachments(self, attachments: Union[List[dict], dict]) -> dict:
        if type(attachments) is not list:
            attachments = [attachments]

        async with aio.ClientSession(trust_env=self.TRUST_ENV, auth=self.AUTH) as session:
            if NFO:
                logger.info(f'Getting attachment(s)...')

            tasks = [asyncio.create_task(self.__get_attachment(session=session, attachment=aid)) for aid in
                     attachments]
            results = await asyncio.gather(*tasks)

            if NFO:
                logger.info('\tComplete.')

        await session.close()

        return await self.process_results(results)

    @retry(retry=retry_if_exception_type(aio.ClientError),
           wait=wait_random_exponential(max=RETRY),
           after=after_log(logger, logging.WARNING))
    async def __get_attachment(self, session: aio.ClientSession, attachment: dict) -> Union[dict, aio.ClientResponse]:
        async with self.sem:
            response = await session.get(f'{self.URI_ATTACHMENT}/{attachment["id"]}',
                                         ssl=self.VERIFY_SSL,
                                         proxy=self.PROXY)

            file = realpath(f'/tmp/{uuid4()}')

            if 200 <= response.status <= 299:
                # todo: candidate for session variables (py38)
                with open(file, mode='wb') as tfile:
                    while 1:
                        chunk = await response.content.read(self.CHUNK_SIZE)
                        if chunk:
                            tfile.write(chunk)
                        else:
                            break

                return {**attachment, 'filePath': file}
            elif response.status in [429, 500, 502, 503, 504]:
                raise aio.ClientError
            else:
                return response


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logging.exception(print_exception(*exc_info()))
