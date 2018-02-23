# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
      name='systeminfo',
      version='0.1.0',
      description='Test for assignment2',
      long_description=readme,
      author='Jiali Yu',
      author_email='jiali.yu@ucdconnect.ie',
      url='https://github.com/Yulia727/systeminfo.git',
      license=license,
      get_package_data= True,
      packages=['systeminfo'],
)


entry_points={
    'console_scripts':['systeminfo=systeminfo.main:main']
}
