import os
import logging
from pathlib import Path  # Path to handle differnrt styles of defining directories & files distinations in CLI, cmd/bash


# src -> folder contains slource code
# components -> folder has several files for the pipeline of different ML project stages, like..data ingesttion, EDA, Feature Engineering, model building, evaluation,...

package_name = "mongodb_connect"

list_of_files = [

    ".github/workflows/ci.yaml", # continouse integration               

    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",

    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",                   # to test one unit or small piece of code runs correctly
    "tests/integration/__init__.py",
    "tests/integration/int.py",      # to test if 2 modules/more of the app/SW run together correctly

    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",

    "experiment/experiments.ipynb"              # for trying/testing a code in Jupyter notebook
    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":  #if the file directory is not empty 
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass # to just create the empty file, fill with code later