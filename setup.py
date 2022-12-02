from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Multiple colour snowfall'
LONG_DESCRIPTION = 'Displaying snowfall in different colours'

# Setting up
setup(
    name="snowflake",
    version=VERSION,
    author="Bipin Yadav",
    author_email="bipin.yadav@fau.de",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy', 'turtle', 'snowflake'],
    keywords=['python', 'snow', 'snowfall', 'colour'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: DSSS professor",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)