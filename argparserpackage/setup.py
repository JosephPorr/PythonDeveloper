# use this command for postgres feed and aws. You can upload all your modules, 
# packages in one go with a single Python Wheel file in the cloud environment you are working on


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

# $ python setup.py bdist_wheel  (build distrobution wheel)
# $ ls dist  (use the ls dist to ensure the distrobution is loaded and where to install the wheel to the venv)
# PythonDeveloper-0.1.0-py3-none-any.whl
# $ pip uninstall pgbackup
# $ pip install dist/pythondeveloper-0.1.0-py3-none-any.whl


# We can use pip to install wheels from a local path, but it can also install from a remote source over HTTP. 
# Let's upload our wheel to S3 and then install the tool outside of our virtualenv from S3:

# $ python
# >>> import boto3
# >>> f = open('dist/pythondeveloper-0.1.0-py3-none-any.whl', 'rb')
# >>> client = boto3.client('s3')
# >>> client.upload_fileobj(f, 'python-backups', 'pythondeveloper-0.1.0-py3-none-any.whl')
# >>> exit()
# We'll need to go into the S3 console and make this file public so that we can download it to install.

# Let's exit our virtualenv and install pgbackup as a user package:

# $ exit
# pip install pre-commit
# $ pip3.7 install --user https://s3.amazonaws.com/python-developer/pgbackup-0.1.0-py3-none-any.whl
# $ pgbackup --help 