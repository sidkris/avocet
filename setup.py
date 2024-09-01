from setuptools import setup, find_packages
from .cryptlib import CryptLib

setup(
    name="cryptlib",
    version="1.0",
    description="An easy to use Python package for encryption and decryption needs",
    author="Siddharth Krishnan",
    email="sid@sidkrishnan.com",
    license="MIT",
    install_requires=["cryptodomex"],
    packages=find_packages(),
)
