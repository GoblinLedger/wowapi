from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='wowapi',
    version='0.4.0',
    packages=['wowapi'],
    install_requires=[
        'requests',
        'certifi'
    ],
    cmdclass={'test': PyTest},
    tests_require=['pytest'],
    test_suite='tests.test_wowapi',
    extra_require={
        'testing': ['pytest'],
    },
    author = "Billy Overton",
    author_email = "billy@billyoverton.com",
    description = "Python library for the World of Warcraft Community API",
    license = "MIT License",
    keywords = "World of Warcraft",
    url = "https://github.com/GoblinLedger/wowapi",

    classifiers= [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Games/Entertainment'
    ]
)
