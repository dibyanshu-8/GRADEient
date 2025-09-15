import os # Importing 'os' module to interact with the operating system, like creating file paths.
import sys # Importing 'sys' module to access system-specific parameters and functions, used here for exception handling.
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # Import the dataclass decorator for automatically generating special methods like __init__().
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass # Use the dataclass decorator to automatically create a class for storing configuration data.
class DataIngestionConfig:
    # Define the file path for the training data CSV, placing it in an 'artifacts' folder.
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    # Define the file path for the testing data CSV, also in the 'artifacts' folder.
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    # Define the file path for the raw (original) data CSV, also in the 'artifacts' folder.
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

# Define the main class responsible for handling the data ingestion process.
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    # Define the method that starts the entire data ingestion process.
    def initiate_data_ingestion(self):
        # Log an informational message indicating the start of the data ingestion process.
        logging.info("Entered the data ingestion method or component")
        # Start a 'try' block to handle potential errors during the process.
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            # Log a message confirming that the dataset has been successfully read into a DataFrame.
            logging.info('Read the dataset as dataframe')
            
            # Create the 'artifacts' directory if it doesn't already exist.
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            # Save the entire original DataFrame to a new CSV file as the raw data.
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            # Log a message indicating that the train-test split process is about to begin.
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            # Log a message confirming that the data ingestion process has completed successfully.
            logging.info("Ingestion of the data is completed")
            # Return the file paths for the newly created train and test data files.
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        # If any exception occurs in the 'try' block, catch it.
        except Exception as e:
            # Raise a custom exception with the error message and system information.
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
    
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))