from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='PythonDeveloper',
    version='0.1.0',
    author='Joseph Porr',
    author_email='usmarine1978@gmail.com',
    description='A utility for backing up code',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JosephPorr',
    packages=find_packages('argparserpackage'), # map the src folder to dir
    packages_dir={'': 'argparserpackage'}, # dic maping to an empty string
    install_requires=['boto3'], # package dependencies
    entry_points={
        'console_scripts': [
            'argparserpackage=argparserpackage.cli:main', # Name of the executable or function to run.  If it's in a module (cli.py) and the function 'main' inside the module.
        ],
    }
)