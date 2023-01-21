from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
import sys
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation


def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        # data_validation_config = Configuration().get_data_transformation_config()
        # print(data_validation_config)
        # schema_file_path = r"F:\Python Classes\ML_class\Machine_Learning_Projects_class\machine_learning_project\config\schema.yaml"
        # file_path = r"F:\Python Classes\ML_class\Machine_Learning_Projects_class\machine_learning_project\housing\artifact\data_ingestion\2022-12-31-16-03-01\ingested_data\test\housing.csv"

        # df=DataTransformation.load_data(file_path=file_path, schema_file_path=schema_file_path)
        # print(df.columns)
        # print(df.dtypes)

    except Exception as e:
        logging.error(f"{e}")
        #raise HousingException (e,sys) from e
        print(e)

if __name__=="__main__":
    main()
 