import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='magento-python',
      version='0.1.0',
      description='API wrapper for Magento Graph written in Python',
      long_description=read('README.md'),
      url='https://github.com/GearPlug/magento-python',
      author='Miguel Ferrer',
      author_email='ingferrermiguel@gmail.com',
      license='GPL',
      packages=['magento'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
