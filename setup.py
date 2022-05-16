from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='baltimore_value_per_acre_analysis',
    package_dir={"": "src"},
    packages=find_packages('src'),
    version='0.0.0',
    description='A way to measure the fiscal sustainability of local land use practices',
    long_description=long_description,
    author='William Fedder and Anna Fedder',
    license='Apache 2.0',
)
