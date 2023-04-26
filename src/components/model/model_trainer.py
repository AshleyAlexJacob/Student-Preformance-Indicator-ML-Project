"""
It contains all the code for training the model

push the model (model_pusher can also be made)

generating confusion matrix for classification

R2 for regressiom
"""

import os
import sys
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info('Split Training and Testing Input Data')
            X_train,y_train,X_test,y_test = (train_array[:,:-1], 
                                             train_array[:,-1],
                                             test_array[:,:-1],
                                             test_array[:,-1]
                                             )
            # initializing models dictionary

            models = {
                'Random Forest':RandomForestRegressor(),
                'Decision Tree':DecisionTreeRegressor(),
                'Gradient Boosting':GradientBoostingRegressor(),
                'Linear Regression':LinearRegression(),
                'K-Neighbors Regressor':KNeighborsRegressor(),
                'XGB Regressor':XGBRegressor(),
                'Catboost Regressor':CatBoostRegressor(),
                'Adaboost Regressor':AdaBoostRegressor(),
            }

            model_report:dict = evaluate_model(X_train=X_train,y_train=y_train,
                                               models=models,X_test= X_test,y_test=y_test)
            # retrieve the best model score
            best_model_score  = max(sorted(model_report.values()))

            # retrieve the best model
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException('No best model found',sys)
            logging.info("Best Model Found on both training and testing dataset")

            save_object(file_path=self.model_trainer_config.trained_model_path,
                        obj=best_model)

            predicted = best_model.predict(X_test)
            return r2_score(y_test,predicted)
        
        except Exception as e:
            raise CustomException(e,sys)

