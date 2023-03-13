from setuptools import find_packages,setup
from typing import List

# declaring constant

HYPHEN_DOT_E= '-e .'

def get_requirements(file_path:SystemError)->List[str]:
    # this function will return a list of requirements
    
    requirements=[]

    with open(file_path) as f:
        requirements = f.readlines()
        [requirement.replace('\n',"") for requirement in requirements ]
    
    if HYPHEN_DOT_E in requirements:
        requirements.remove(HYPHEN_DOT_E)
    
    return requirements



setup(
    name='Student_Performance_Indicator',
    version='0.0.1',
    author='Ashley Alex Jacob',
    author_email='alexjacob260@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

