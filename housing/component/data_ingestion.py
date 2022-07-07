import logging
from tkinter import E
from housing.entity.config_entity import DataIngestionConfig
from housing.entity.artifact_entity import DataIngestionArtifact
import sys,os
from housing.exception import HousingException
from housing.logger import logger
import tarfile
from six.moves import urllib


class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20}DataIngestion log started.{'='*20} ")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise HousingException(e,sys) from e 

    def download_housing_data(self)->str:
        try:
            # extraction remote url to download dataset
            download_url = self.data_ingestion_config.dataset_download_url

            # folder location download file
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir

            housing_file_name = os.path.basename(download_url)

            tgz_file_path = os.path.join(tgz_download_dir,housing_file_name)
            logging.info(f"Downloading File from :[{download_url}] into:[{tgz_file_path}]")
            urllib.request.urlretrieve(download_url,tgz_file_path)
            logging.info(f"File : [{tgz_file_path}] has been downloaded successfully")

            return tgz_file_path


        except Exception as e:
            raise HousingException(e,sys) from e

    def extract_tgz_file(self):
        pass

    def split_data_as_train_test(self):
        pass

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e 