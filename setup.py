from setuptools import setup
from .crypt_lib import Cryptography

setup(
    name="cryptography",
    version="1.0",
    description="An easy to use Python package for encryption and decryption needs",
    author="Siddharth Krishnan",
    email="sidkrishnan@protonmail.com",
    license="MIT",
    # url="https://github.com/sidkrishnan/crypt",
    install_requires=["cryptodomex"],
    packages=["crypt"],
)
