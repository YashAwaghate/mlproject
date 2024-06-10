from setuptools import find_packages, setup
from typing import List

HYPHN_E = '-e .'
def get_requirements(file_path: str)-> List[str]:
    """
    This function will return the list of requiremnets.
    """
    requirements = []
    with open(file_path )as file_object:
        requirements = file_object.readlines()
        print(requirements)
        [req.replace("\n",  "") for req in requirements ]
        if HYPHN_E in requirements:
            requirements.remove(HYPHN_E)

    return requirements
    

setup(
    name='mlproject',
    version='0.1',
    author='Yash Awaghate',
    author_email='awaghate.yash@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)