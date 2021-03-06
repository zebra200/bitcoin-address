from setuptools import setup

__name__ = 'bitcoinaddress'
__version__ = '0.0.1'
__author__ = 'Jesse Panganiban'

install_requires = [
    'argparse',
    'pyzmq',
]


setup(name=__name__,
      version=__version__,
      author=__author__,
      install_requires=install_requires,
      pymodules=['bitcoinaddress'])
