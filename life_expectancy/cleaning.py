import pandas as pd
from life_expectancy.regions import Region

def clean_data(data_to_clean: pd.DataFrame, country: Region = Region.PT) -> pd.DataFrame:
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
    return cleaned_data[cleaned_data['region'] == country.name]
