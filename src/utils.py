#utils will have all the common things that we are going to import and use
import os
import sys
import numpy as np
import pandas as pd
import dill

from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(X,y,models):
    try:
        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
        
        report={}
        