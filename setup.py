"""cdk-utils setup"""

from cdk_utils import __version__
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cdk-utils',
    version=__version__,
    description='Helper functions for use with python AWS-CDK',
    long_description=long_description,
    url='https://github.com/ucopacme/cdk-utils',
    author='Ashley Gould',
    author_email='agould@ucop.edu',
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='aws cdk',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'PyYAML', 
    ],
)
