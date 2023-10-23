from setuptools import setup, find_namespace_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.5"
AUTHOR="Jay Bhesania"
DESCRIPTION="This is first Machine Learning Project"

REQUIREMENT_FILE_NAME="requirements.txt"

HYPHEN_E_DOT = "-e ."

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file

    return This function is going to return a list which will contain name
    of libraries mentioned in the requirements.txt file
    """
    # with open(REQUIREMENTS_FILE_NAME) as requirement_file:
    #     return requirement_file.read().splitlines().remove("-e .")
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        return requirement_list


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_namespace_packages(),
install_requires=get_requirements_list()

)
