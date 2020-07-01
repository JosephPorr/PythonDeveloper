from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup'
    version='0.1.0',
    authoer='Joseph Porr'
    author_email='Joseph.Porr@gmail.com',
    description='A utility for backing up PostgreSQL databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JosephPorr/PythonDeveloper',
    packages=find_packages('src')
)