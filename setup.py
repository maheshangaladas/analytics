import os
from setuptools import setup
from setuptools import find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="analytics",
    version="0.0.1",
    author="Wilfried N'Guessan",
    author_email="wilfried.nguessan@outlook.com",
    description="TBA",
    license="MIT",
    keywords="example documentation tutorial",
    url="http://packages.python.org/an_example_pypi_project",
    # packages=['package_name', 'package_name'],
    long_description=read("README"),
    install_requires=[line.rstrip("\n") for line in open("requirements.txt")],
)
