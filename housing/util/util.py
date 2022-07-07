import imp


import yaml
from housing.exception import HousingException
import os,sys

def read_yaml(file_path:str)->dict:
    '''
    Read yaml file and return the dictionary
    '''
    try:
        with open(file_path,'rb') as yaml_file:
            return  yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e