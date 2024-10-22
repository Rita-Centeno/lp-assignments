import argparse
import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    '''
    Loads the data from a given path.
    
    Args:
        path (str): The path to the data file.

    Returns:
        pd.DataFrame: The loaded data.
    '''
    return pd.read_csv(path, sep='\t')

def clean_data(data_to_clean: pd.DataFrame, country: str = 'PT') -> pd.DataFrame:
    '''
    Cleans the data. Unpivots the data, removes NaNs, and filters only the data 
    where region equals to PT (Portugal).
    
    Args:
        data_to_clean (pd.DataFrame): The data to be cleaned.
        country (str): The country code to filter the data by. Default is 'PT'.
    
    Returns:
        pd.DataFrame: The cleaned data.
    '''

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
    '''
    Saves data to the given data folder.
    
    Args:
        data_to_save (pd.DataFrame): The data to be saved.
        output_path (str): The path to save the data to.
    '''

    return data_to_save.to_csv(path, index=False)

def main(filter_country: str,
         input_path: str = 'life_expectancy/data/eu_life_expectancy_raw.tsv',
         output_path: str = 'life_expectancy/data/pt_life_expectancy.csv') -> None:
    '''
    Main function to load, clean and save the data.

    Args:
        filter_country (str): The country code to filter the data by.
        input_path (str): The path to the data file.
        output_file (str): The path to save the cleaned data.
    '''

    loaded_data = load_data(path=input_path)
    cleaned_data = clean_data(data_to_clean=loaded_data, country=filter_country)
    save_data(data_to_save=cleaned_data, path=output_path)

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument('--country', type=str, default='PT', help='Country code (default: PT)')
    parser.add_argument('--input_path', type=str,
            default='life_expectancy/data/eu_life_expectancy_raw.tsv',
            help='Path to the data file')
    parser.add_argument('--output_path', type=str,
            default='life_expectancy/data/pt_life_expectancy.csv',
            help='Path to save the cleaned data')
    args = parser.parse_args()
    main(args.country, args.input_path, args.output_path)
