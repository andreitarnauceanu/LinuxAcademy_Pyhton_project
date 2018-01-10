from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()
setup(
        name='pgbackup',
        version='0.1.0',
        description='Database backups locally or on S3.',
        long_description=readme;
        author='Andrei Tarnauceanu',
        author_email='linuxacademystudent@gmail.com',
        packages=find_packages('src')
        package_dir={'': 'src'},
        install_requires=[]
    )
