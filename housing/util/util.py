
#util.py stores all the functions which are not part of main pipeline but are required for functioning of main task.
#We can also say util.py stores all the helper functions (e.g reading yaml file, reading pickel files, etc)

import yaml
from housing.exception import HousingException 
import os,sys

# creating a function to read yaml file
def read_yaml_file (file_path: str) -> dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException (e,sys) from e


