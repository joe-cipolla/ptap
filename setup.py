from setuptools import setup, find_packages
import os

# load python startup script (preloads packages and settings)
filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
    with open(filename) as fobj:
        startup_file = fobj.read()
    exec(startup_file)

# sets version
main_ns = {}
ver_path = (os.path.dirname(os.path.abspath(__file__)) + '\\').replace('\\', '/') + 'nyiso_sql/_version.py'
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setup(
    name='nyiso_sql',
    version=main_ns['__version__'],
    author='Joe Cipolla',
    author_email='jlcipolla@gmail.com',
    console_scripts=[''],
    packages=find_packages(),
    url='',
    license='LICENSE.txt',
    description='Library that scrapes, cleans, and loads NYISO data into PostgreSQL db.',
    long_description=open('README.md').read(),
    python_requires='>=3.7',
    install_requirements=[
        'pandas', 'numpy', 'psycopg2', 'zipfile'
    ],
    classifiers=[
        "Programming language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    keywords=['nyiso', 'PostgreSQL']
)
