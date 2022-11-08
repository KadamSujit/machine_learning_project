from setuptools import setup, find_packages
from typing import List

#Declaring variable for setup functions
PROJECT_NAME = "housing-predictor"
VERSION =  "0.0.3"
AUTHOR = "Sujit Kadam"
DESCRIPTION = "This is the first machine learning project for FSDS Nov 21 batch using CICD pipeline"
#PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list() -> List[str]:
    """
    Description: This function is will return list of requirements
    mentioned in requirements.txt file

    return: It will return a list which contains name of libraries mentioned in
    requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
       return requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    #packages=PACKAGES,
    packages=find_packages(),
    install_requires=get_requirements_list()

)
 