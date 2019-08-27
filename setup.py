import os
from setuptools import setup
from setuptools import find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "project_name",
    version = "0.0.0",
    author = "Name Surname",
    author_email = "name.surname@mail.com",
    description = "Short description",
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['package_name', 'package_name'],
    long_description=read('README'),
    install_requires=[line.rstrip("\n") for line in open("requirements.txt")],
)