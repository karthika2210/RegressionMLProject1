# setup.py: To convert the project folder in to packages
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

# new form of writing function in python 3.8 
# ie; we can mention the type of parameter and the return type of function
def get_requirements(file_path:str)-> List[str]:
    requirements = []
    # open the requirements.txt
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name = 'RegressorProject',
    version = '0.0.1',
    author = 'Karthika',
    author_email = 'karthikaravi7879@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages = find_packages()
)