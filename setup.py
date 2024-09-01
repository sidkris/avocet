from setuptools import setup, find_packages

setup(
    name="pycryptlibrary",
    version="1.0",
    description="An easy to use Python package for encryption and decryption needs",
    author="Siddharth Krishnan",
    author_email="sid@sidkrishnan.com",
    license="MIT",
    install_requires=["pycryptodomex"],
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
