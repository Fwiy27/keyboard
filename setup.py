from setuptools import setup, find_packages

setup(
    name = 'kbd',
    version = '1.0.2',
    description = "Custom Implementation of pynput's Keyboard",
    long_description = open('README.md').read(),
    author = 'Landon Migawa',
    author_email = 'landonmigawa27@gmail.com',
    maintainer = 'Landon Migawa',
    maintainer_email = 'landonmigawa27@gmail.com',
    packages = find_packages(include = ['kbd']),
    install_requires = ['pynput', 'numpy'],
    python_requires = ">=3.7"
)