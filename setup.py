#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


install_requires = []
# install_requires = ['requests >= 2.1.0']

# For SNI support in Python 2, must install the following packages
# if sys.version_info[0] == 2:
#     install_requires.append('pyOpenSSL >= 0.14')
#     install_requires.append('ndg-httpsclient >= 0.3.3')
#     install_requires.append('pyasn1 >= 0.1.7')

setup(
    name='mymodule',
    packages=['mymodule'],
    version='0.1',
    description='Desc',
    long_description=(read('README.rst') + '\n\n' +
                      read('HISTORY.rst') + '\n\n' +
                      read('AUTHORS.rst')),
    url='http://github.com/rgooler/bootstrap-pip/',
    license='MIT',
    author='Ryan Gooler',
    author_email='ryan.gooler@gmail.com',
    py_modules=['mymodule'],
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
