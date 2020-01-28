#!/usr/bin/env python3.8
"""Phishlabs API Client: Models.Query
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

from dataclasses import dataclass
from typing import List, Optional, Union

import re

from base_api_client.models.record import Record

import datetime as dt


@dataclass
class Query(Record):
    caseType: Optional[List[str]] = None
    dateBegin: Optional[str] = None
    dateEnd: Optional[str] = None
    dateField: Optional[str] = None
    format: Optional[str] = 'json'
    maxRecords: Optional[int] = 200  # Max set by API
    offset: Optional[int] = 0

    def params(self, offset: Optional[int] = None):
        # todo: we can probably replace this with a multi-dict?
        if offset:
            self.offset = offset

        params = []
        for k, v in self.dict().items():
            if type(v) is list:
                for item in v:
                    params.append((k, item))
            else:
                params.append((k, v))
