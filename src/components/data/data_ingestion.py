"""
It contains all the code for loading the data from databases or any other sources

also the splitting of data into train,test and validation sets

"""

import os
import sys
# importing custom exception
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data.data_transformation import DataTransformation,DataTransformationConfig

from src.components.model.model_trainer import ModelTrainerConfig, ModelTrainer

# all the inputs required for Data Ingestion Component will be added to this class

@dataclass
class DataIngestionConfig:
    train_data_path:str =os.path.join('artifacts',"train.csv")
    test_data_path:str =os.path.join('artifacts',"test.csv")
    raw_data_path:str =os.path.join('artifacts',"data.csv")
    
class DataIngestion:
    def __init__(self) :
        self.ingestion_config = DataIngestionConfig()
    
    # my own function
    def initiateDataIngestion(self):
        logging.info('Entered the Data Ingestion Method or Component')
        try:
            df = pd.read_csv('notebooks/DATA/StudentsPerformance.csv')
            logging.info('Read the dataset as dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info('Train Test Split Initiated')
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)




if __name__ == "__main__":
    # combined Data Ingestion
    obj = DataIngestion()
    train_data,test_data = obj.initiateDataIngestion()
    # combined Data Transformation
    data_transformation = DataTransformation()
    train_arr,test_arr,_= data_transformation.initiate_data_transformation(train_data,test_data)
    # model trainer
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr))





