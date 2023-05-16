from setuptools import setup

setup(
    name='file-managers',
    version='0.1',
    author='Md. Musfiqur Rahaman',
    author_email='musfiqur.rahaman@northsouth.edu',
    description='This will help you to manage your files and folders easily in different ways.',
    packages=['file_managers'],
    install_requires=[
        'numpy',
        'pandas'
    ]
)
