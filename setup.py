import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="analytics",
    version="0.1.4",
    author="Wilfried N'Guessan",
    author_email="wilfried.nguessan@outlook.com",
    description="Web analytics tooling",
    license="GNU GPLv3",
    keywords="analytics google",
    url="https://github.com/xslates/analytics",
    long_description=read("README.md"),
    install_requires=[line.rstrip("\n") for line in open("requirements.txt")],
)
