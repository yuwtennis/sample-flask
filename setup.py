
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

setup(
    name='flaskr',
    version='0.0.1',
    description='Personal getting started with Flask',
    author='Yu Watanabe',
    packages=find_packages(),
    python_requires='>=3.5, <4',
    install_requires=['Flask', 'waitress'],
)
