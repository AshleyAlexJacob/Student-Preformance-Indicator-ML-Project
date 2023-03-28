"""
It contains all the code related to commonly used code over the entire project

for example:

mongo client for reading code from mongodb

save the model in cloud

"""
import os
import sys
import dill
from src.exception import CustomException
import pandas as pd
import numpy as np


def save_object(file_path:str,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)


