try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description = '''
Python implementation of RakNet 3.25. This is not aimed to be a complete port of RakNet,
just everything that's needed to run a server.
'''

setup(
    name="PyRakNet",
    version="1.0.0",
    description="Minimal Python implementation of RakNet 3.25.",
    long_description=long_description,
    author="Jordan Maxwell",
    url="https://github.com/StellarGaming/pyraknet",
    license="GPL v3",
    packages=["pyraknet"],
    classifiers=[
        'Programming Language :: Python :: 3'
    ])
