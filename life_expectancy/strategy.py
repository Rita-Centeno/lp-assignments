from abc import ABC, abstractmethod
import pandas as pd
from life_expectancy.regions import Region
from life_expectancy.loading_saving import load_data, load_data_json, save_data
from life_expectancy.cleaning import clean_data, clean_data_json

class DataStrategy(ABC):
    """Abstract class for data loading, cleaning and saving strategies"""
    @abstractmethod
    def load_data_strategy(self, path: str):
        """Loads the data from a given path"""

    @abstractmethod
    def clean_data_strategy(self, data: pd.DataFrame, country: Region):
        """Cleans and filters the data"""

    @abstractmethod
    def save_data_strategy(self, data: pd.DataFrame, path: str):
        """Saves the data to a given path"""


class TsvDataStrategy(DataStrategy):
    """Concrete class for TSV data loading, cleaning and saving strategies"""
    def load_data_strategy(self, path: str) -> pd.DataFrame:
        return load_data(path)

    def clean_data_strategy(self, data: pd.DataFrame, country: Region) -> pd.DataFrame:
        return clean_data(data, country)

    def save_data_strategy(self, data: pd.DataFrame, path: str) -> None:
        save_data(data, path)


class JsonDataStrategy(DataStrategy):
    """Concrete class for JSON data loading, cleaning and saving strategies"""
    def load_data_strategy(self, path: str) -> pd.DataFrame:
        return load_data_json(path)

    def clean_data_strategy(self, data: pd.DataFrame, country: Region) -> pd.DataFrame:
        return clean_data_json(data, country)

    def save_data_strategy(self, data: pd.DataFrame, path: str) -> None:
        save_data(data, path)


def get_strategy(file_path: str):
    """Determine the appropriate strategy based on the file extension"""
    if file_path.endswith('.tsv'):
        return TsvDataStrategy()
    if file_path.endswith('.json'):
        return JsonDataStrategy()
    raise ValueError(f"Unsupported file extension for file: {file_path}")
