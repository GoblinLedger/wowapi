from setuptools import setup, find_packages

setup(
    name='wowapi',
    version='0.1.0',
    packages=['wowapi'],
    install_requires=[
        'requests',
        'certifi',
        'wsgiref'
    ],

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
