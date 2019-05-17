#!/usr/bin/env python3.7
"""LibSEA Phishlabs: Setup
   Jerod Gawne, 2019.03.20 <https://github.com/jerodg/>"""
import logging
import sys
import traceback

import setuptools

logger = logging.getLogger(__name__)
name = 'libsea_phishlabs'


# todo: create documentation
# todo: create tests
# todo: rewrite readme in markdown

def readme() -> str:
    with open('README.adoc') as f:
        return f.read()


if __name__ == '__main__':
    try:
        setuptools.setup(name='libsea_phishlabs',
                         version='1.0b0.dev0',
                         description='Phishlabs API Client Library',
                         long_description=readme(),
                         long_description_content_type='text/markdown',
                         classifiers=['Development Status :: 4 - Beta',
                                      'Environment :: Console',
                                      'Intended Audience :: End Users/Desktop',
                                      'Intended Audience :: Developers',
                                      'Intended Audience :: System Administrators',
                                      'License :: Other/Proprietary License',
                                      'Natural Language :: English',
                                      'Operating System :: MacOS :: MacOS X',
                                      'Operating System :: Microsoft :: Windows',
                                      'Operating System :: POSIX',
                                      'Programming Language :: Python',
                                      'Topic :: Utilities'],
                         keywords='api client phishlabs',
                         url='https://github.info53.com/Fifth-Third/SEA-LibSEA_PhishLabs',
                         author='Jerod Gawne',
                         author_email='jerodgawne@gmail.com',
                         license='Other/Proprietary',
                         packages=setuptools.find_packages(),
                         install_requires=['aiohttp', 'aiodns', 'cchardet', 'libsea_base', 'tenacity'],
                         include_package_data=True,
                         zip_safe=True,
                         setup_requires=['pytest-runner'],
                         tests_require=['pytest', 'pytest-cov', 'pytest-asyncio'],
                         scripts=[],
                         entry_points={'console_scripts': []},
                         python_requires='~=3.7',
                         project_urls={
                             'Documentation': 'https://github.info53.com/Fifth-Third/SEA-LibSEA_Phantom/tree/master/docs'})
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))
