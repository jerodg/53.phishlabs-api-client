#!/usr/bin/env python3.7
"""LibSEA Base Tests Init: Jerod Gawne, 2019.03.14 <https://github.com/jerodg/>"""
import logging
import sys
import traceback

from libsea_phishlabs.tests import test_get_case_count

___all___ = ['test_phishlabs_api']

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)

if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))
