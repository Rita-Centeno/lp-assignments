import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    '''Loads the data from a given path'''

    return pd.read_csv(path, sep='\t')

def save_data(data_to_save: pd.DataFrame, path: str) -> None:
    '''Saves data to the given data folder'''

    return data_to_save.to_csv(path, index=False)
