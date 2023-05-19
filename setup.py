from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='file-managers',
    version='0.22.0',
    author='Md. Musfiqur Rahaman',
    author_email='musfiqur.rahaman@northsouth.edu',
    description='A Python Package to manage your files and folders easily in different ways.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['file_managers'],
    install_requires=['twine', 'wheel'],
    url='https://github.com/MusfiqDehan/file-managers'
)
