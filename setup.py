"""
FlaskBB
=======

FlaskBB is a Forum Software written in Python using the micro framework Flask.


Quickstart
----------

.. code:: bash

    # Install the FlaskBB package and it's dependencies
    $ pip install -e .

    # Generate a configuration
    $ flaskbb makeconfig

    # Install FlaskBB
    $ flaskbb install

    # Run the development server
    $ flaskbb run
     * Running on http://localhost:8080/


Resources
---------

* `website <https://flaskbb.org>`_
* `source <https://github.com/sh4nks/flaskbb>`_
* `issues <https://github.com/sh4nks/flaskbb/issues>`_
"""
import ast
import os
import re
import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


class PyTestCommand(TestCommand):
    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest  # noqa
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def get_requirements(e=None):
    rf = "requirements.txt" if e is None else 'requirements-{}.txt'.format(e)
    r = read(rf)
    return [x.strip() for x in r.split('\n')
            if not x.startswith('#') and not x.startswith("-e")]


install_requires = get_requirements()


setup(
    name='FlaskBB',
    version="2.0.0.dev0",
    url='https://github.com/sh4nks/flaskbb/',
    license='BSD',
    author='Peter Justin',
    author_email='peter.justin@outlook.com',
    description='A classic Forum Software in Python using Flask.',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    entry_points='''
        [console_scripts]
        flaskbb=flaskbb.cli:flaskbb
    ''',
    test_suite='tests',
    tests_require=[
        'py',
        'pytest',
        'pytest-cov',
        'cov-core',
        'coverage'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    cmdclass={'test': PyTestCommand}
)
