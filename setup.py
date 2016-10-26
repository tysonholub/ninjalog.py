import ninjalog
from setuptools import setup

setup(name='ninjalog',
      version=ninjalog.__version__,
      description='A Python logging handler for https://www.ninjalog.io',
      url='https://www.ninjalog.io',
      author='Tyson Holub',
      author_email='tyson@tysonholub.com',
      license='MIT',
      packages=['ninjalog'],
      install_requires=[
        'requests',
        'grequests',
        'pyjwt',
      ])
