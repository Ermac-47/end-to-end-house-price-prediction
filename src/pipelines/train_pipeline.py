import sys
from src.logger import logging
from src.exception import Custom_Exception

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class TrainPipeline:
    def __init__(self):
        pass

    def run_pipeline(self):
        try:
            logging.info("===== Training Pipeline Started =====")

            # 1. Data Ingestion
            ingestion = DataIngestion()
            train_data_path, test_data_path = ingestion.initiate_data_ingestion()

            logging.info("Data ingestion completed")

            # 2. Data Transformation
            transformation = DataTransformation()
            train_arr, test_arr, _ = transformation.initiate_data_transformer(
                train_data_path, test_data_path
            )

            logging.info("Data transformation completed")

            # 3. Model Training
            trainer = ModelTrainer()
            r2_score = trainer.initiate_model_trainer(train_arr, test_arr)

            logging.info(f"Model training completed with R2 Score: {r2_score}")

            logging.info("===== Training Pipeline Completed Successfully =====")

            return r2_score

        except Exception as e:
            raise Custom_Exception(e, sys)


if __name__ == "__main__":
    pipeline = TrainPipeline()
    print("Training R2 Score:", pipeline.run_pipeline())
