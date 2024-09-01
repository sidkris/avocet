from setuptools import setup
from .crypt_lib import Cryptography

setup(
    name="cryptography",
    version="1.0",
    description="An easy to use Python package for encryption and decryption needs",
    author="Siddharth Krishnan",
    email="sid@sidkrishnan.com",
    license="MIT",
    install_requires=["cryptodomex"],
    packages=["crypt"],
)
