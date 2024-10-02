from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements

    we have also added the -e . constant at the end of the requirements.txt file because the name of the packages written there only get installed but we want them to get build too simultaneously for which we write this constant at the end of requirements.txt file
    
    '''

    HYPEN_E_DOT = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', ' ') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name = 'mini project',
version = '0.0.1',
author = 'NikhilNagaich',
author_email = 'nikharynagaich29.jan@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')

)