from setuptools import setup, find_packages
# setuptools is a package used by many other packages to handle their installation from source code (and tasks related to it).
# It is generally used extensively for non-pure-Python packages, which need some compilation/installation step before being
# usable (think packages containing extensions written in C); 
# setuptools factors away some of the most common operations used in this process (compiling C files with options compatible with the..
#  ..current Python installation, running Cython if required, provide some vaguely coherent set of commands/options for 
# setup.py files, ...) as well as providing some tools used during Python packages development.
# There is some kind of overlap with distutils, distutils2 (?) and some of the other packages setup tools 

from typing import List
# typing: improve code readability and maintainability: Type hints make code more self-documenting, as they explicitly state the 
# expected types of variables, functions, and other code elements. 


HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [line.replace('\n', '') for line in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


__version__ = "0.0.1"
REPO_NAME = "mongodb_connector" # the repo name in github
PKG_NAME = "MongoDB-Connect"  # this python package will show in this name on PyPi packages repos website https://pypi.org/
AUTHOR_USER_NAME = "MohamedEmam82"
AUTHOR_EMAIL = "mohamed_salaheldin_emam@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    # https://github.com/MohamedEmam82/mongodb_proj
    project_urls={"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",},
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("./requirements_dev.txt"),

)


