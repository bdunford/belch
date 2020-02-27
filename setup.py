from setuptools import setup

setup(name='belch',
    version='0.1',
    description='For parsing, searching, and generatig python scripts from burp output',
    url='https://github.com/bdunford/belch/',
    author='b1rch',
    author_email='birch.dunford@gmail.com',
    license='MIT',
    packages=['belch'],
    zip_safe=False,
    scripts=['bin/belch'],
    install_requires=[]
)
