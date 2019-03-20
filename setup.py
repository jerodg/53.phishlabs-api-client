#!/usr/bin/env python3.7
"""LibSEA Phishlabs Setup: Jerod Gawne, 2019.03.20 <https://github.com/jerodg/>"""
import logging
import sys
import traceback

import setuptools

logger = logging.getLogger(__name__)
name = 'libsea_phishlabs'


def readme() -> str:
    with open('README.adoc') as f:
        return f.read()


if __name__ == '__main__':
    try:
        setuptools.setup(name='libsea_phishlabs',
                         version='1.0a0.dev0',
                         description='Phishlabs API Client Library',
                         long_description=readme(),
                         long_description_content_type='text/markdown',
                         classifiers=[
                             'Development Status :: 3 - Alpha',
                             'Environment :: Console',
                             'Intended Audience :: End Users/Desktop',
                             'Intended Audience :: Developers',
                             'Intended Audience :: System Administrators',
                             'License :: OSI Approved :: GNU Affero General Public License v3',
                             'Natural Language :: English',
                             'Operating System :: MacOS :: MacOS X',
                             'Operating System :: Microsoft :: Windows',
                             'Operating System :: POSIX',
                             'Programming Language :: Python',
                             'Topic :: Utilities'],
                         keywords='api client base',
                         url='https://github.info53.com/Fifth-Third/SEA_LibSEA_PhishLabs',
                         author='Jerod Gawne',
                         author_email='jerodgawne@gmail.com',
                         license='None/Proprietary',
                         packages=setuptools.find_packages(),
                         install_requires=[],
                         include_package_data=True,
                         zip_safe=False,
                         setup_requires=['pytest-runner'],
                         tests_require=['pytest'],
                         scripts=[],
                         entry_points={'console_scripts': []},
                         python_requires='~=3.7')
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))
