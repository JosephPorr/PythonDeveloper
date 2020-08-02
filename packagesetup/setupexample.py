# When you create new project (new folder), the venviroment needs to be added. 
# If the folder is a child of a parent folder with pipenv, it's already available.
# Need to create a blank __init__.py  in the same folder
# $ pipenv --python python3
# $ pipenv shell to activate the enviroment
# https://docs.python.org/3/distutils/setupscript.html
# The setup script is the centre of all activity in building, distributing, and installing modules using the Distutils. 
# The main purpose of the setup script is to describe your module distribution to the Distutils, 
# so that the various commands that operate on your modules do the right thing.

from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
  readme = f.read()

setup(
    name='hr',
    version='1.0.0',
    description='Command line user export utility',
    long_description=readme,
    author='Your Name',
    author_email='your_email@example.com',
    packages=find_packages('src'),  #  The src is the current folder where the pipenv and packages are located.
    package_dir={'': 'src'},
    install_requires=[]  # THere's no dependencies and empty
)