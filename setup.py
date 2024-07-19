"""
Code based from this page:
https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/
"""
from setuptools import setup, find_packages

setup(
    name='rattle',
    version='0.1.0',    
    description='A toolbox for python',
    url='https://github.com/lucasbanunes/rattle',
    author='lucasbanunes',
    author_email='lucasbanunes@gmail.com',
    license='',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)