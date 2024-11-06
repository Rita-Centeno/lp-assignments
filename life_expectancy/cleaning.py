import os
import argparse
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, 'data')

def load_data(path: str) -> pd.DataFrame:
    '''Loads the data from a given path'''

    return pd.read_csv(path, sep='\t')

def clean_data(data_to_clean: pd.DataFrame, country: str = 'PT') -> pd.DataFrame:
    '''Cleans the data. Unpivots the data, removes NaNs, and filters only the data 
    where region equals to PT (Portugal)'''

    # Unpivot the data
    split_columns = data_to_clean['unit,sex,age,geo\\time'].str.split(',', expand=True)
    data_to_clean[['unit', 'sex', 'age', 'region']] = split_columns
    data_to_clean.drop('unit,sex,age,geo\\time', axis=1, inplace=True)
    year_columns = data_to_clean.columns.to_list()
    cleaned_data = pd.melt(data_to_clean,
                      id_vars=['unit', 'sex', 'age', 'region'],
                      value_vars=year_columns,
                      var_name='year',
                      value_name='value')

    # Clean the data
    cleaned_data['year'] = cleaned_data['year'].astype(int)

    cleaned_data['value'] = cleaned_data['value'].astype(str).str.extract(r'([0-9,.]+)')
    cleaned_data = cleaned_data.dropna(subset=['value'])
    cleaned_data['value'] = cleaned_data['value'].astype(float)

    # Filter the data by country code
    return cleaned_data[cleaned_data['region'] == country]

def save_data(data_to_save: pd.DataFrame, path: str) -> None:
    '''Saves data to the given data folder'''

    return data_to_save.to_csv(path, index=False)

def main(filter_country: str = 'PT') -> None:
    '''Main function to load, clean and save the data'''

    # Define the data paths
    input_path = os.path.join(DATA_PATH, 'eu_life_expectancy_raw.tsv')
    output_file_name = f'{filter_country.lower()}_life_expectancy.csv'
    output_path = os.path.join(DATA_PATH, output_file_name)

    # Load, clean and save the data
    loaded_data = load_data(path=input_path)
    cleaned_data = clean_data(data_to_clean=loaded_data, country=filter_country)
    save_data(data_to_save=cleaned_data, path=output_path)

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument('--country', type=str, default='PT', help='Country code (default: PT)')
    args = parser.parse_args()
    main(args.country)
