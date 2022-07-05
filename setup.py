from setuptools import setup
from typing import List  # in this list we can specify data type


# Declaring variables for setup
PROJECT_NAME = "housing predictor"
VERSION = '0.0.1'
AUTHOR = 'Abhishek Nagpal'
DESCRIPTION = "THIS IS MY FIRST MACHINE LEARNING PROJECT"
PACKAGES = ['housing']
REQUIREMENT_FILE_NAME = 'requirements.txt'

def get_requirements_list()->List[str]:
    """
    this function returns the list of requiremnts 
    mention in requirements.txt

    return This function is going to return a list which contain name of 
    librarires written in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(

name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires = get_requirements_list()


)

