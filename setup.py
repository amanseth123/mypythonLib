from setuptools import find_packages, setup
from distutils.core import setup

setup(
    name = 'my_python_package',
    packages = ['my_python_package'],
    version = 'version number',  # Ideally should be same as your GitHub release tag varsion
    description = 'description',
    author = '',
    author_email = '',
    url = 'github package source url',
    download_url = 'download link you saved',
    keywords = ['tag1', 'tag2'],
    classifiers = [],
)
setup(
    name='myglib',
    packages=find_packages(include=['myglib']),
    version='0.1.0',
    description='My first Python library',
    author='Me',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)