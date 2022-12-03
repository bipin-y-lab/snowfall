from setuptools import setup, find_packages

setup(
    name='snowflake',
    version='0.1',
    packages=find_packages(exclude=['numpy']),
    license='Apache License',
    long_description=open('README.md').read(),
)