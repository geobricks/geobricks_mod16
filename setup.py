from setuptools import setup
from setuptools import find_packages

setup(
    name='GeobricksMOD16',
    version='0.1.0',
    author='Simone Murzilli; Guido Barbaglia',
    author_email='geobrickspy@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='MOD16 Project plug-in for Geobricks downloader.',
    install_requires=[
        'watchdog', 'flask', 'flask-cors'
    ],
    url='http://pypi.python.org/pypi/GeobricksMOD16/'
)
