# import multiprocessing to avoid this bug (http://bugs.python.org/issue15881#msg170215)
import multiprocessing
assert multiprocessing
import re
from setuptools import setup, find_packages


def get_version():
    """
    Extracts the version number from the version.py file.
    """
    VERSION_FILE = '{{ project_name }}/version.py'
    mo = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', open(VERSION_FILE, 'rt').read(), re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError('Unable to find version string in {0}.'.format(VERSION_FILE))


setup(
    name='{{ pypi_name }}',
    version=get_version(),
    description='',
    long_description=open('README.rst').read(),
    url='https://github.com/ambitioninc/{{ repo_name }}',
    author='{{ author_name }}',
    author_email='opensource@ambition.com',
    keywords='',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
    install_requires=[
        'nose>=1.3.0',
    ],
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=[
        'coverage>=3.7.1',
        'mock>=1.0.1',
    ],
    zip_safe=True,
)
