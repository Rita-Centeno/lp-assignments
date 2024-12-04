import json
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    '''Loads the data from a given path'''
    return pd.read_csv(path, sep='\t')


def load_data_json(path: str) -> pd.DataFrame:
    '''Loads the data from a given path in json format'''
    with open(path, 'r',  encoding='utf-8') as file:
        data_json = json.load(file)
        data_json = pd.DataFrame(data_json)
    return data_json


def save_data(data: pd.DataFrame, path: str) -> None:
    '''Saves data to the given data folder'''
    return data.to_csv(path, index=False)
