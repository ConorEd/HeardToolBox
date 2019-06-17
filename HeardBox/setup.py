##
import os
from setuptools import setup, find_namespace_packages
from pkg_resources import get_distribution, DistributionNotFound

def read(fname):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup (
    name = "namespace.HeardBox",
    use_scm_version = True,
    setup_requires=['setuptools_scm'],
    version = "0.0.1",
    author = "Conor Edwards",
    author_email = "conorlo@hotmail.co.uk",
    description = ("Interface the Heard Proteomic Database with Python"),
    url = "http://wwww.github.com/ConorEd/HeardBox",
   # packages['HeardBox', 'tests'],
        #license = "BSD", 
    keywords = "Uniprot Excel Interface, Bioinformatics, Quality of life improvement, BLAST, ALIGN, GO, Excel",
    
    
    long_description=read("README.txt"),
    classifiers=[
        "Development Sttus :: 2 - Pre-Alpha",
        "Topic :: Science",
        "License :: OSI Approved :: BSD License",
        ],
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),

  
    install_requires=['xlwings', 'biopython', 'uniprot_tools'],
    entry_points={
           'console_scripts': [
           'main = HeardBox.main:main_func',
           #'ext_mod = HeardBox._mod:some_func',
            ]
    }
)
#├── setup.py
#├── src
#│   └── namespace
#│       └── mypackage
#│           ├── __init__.py
#│           └── mod1.py
#└── tests
#    └── test_mod1.py