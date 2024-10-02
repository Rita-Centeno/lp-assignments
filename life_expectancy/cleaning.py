import argparse
import pandas as pd

def clean_data(country: str = 'PT'):
    '''Cleans the data and saves the cleaned data to the data folder.'''
    # Load the eu_life_expectancy_raw.tsv data from the data folder
    file_path = 'life_expectancy/data/eu_life_expectancy_raw.tsv'
    df = pd.read_csv(file_path, sep='\t')

    # Unpivot the date to long format, so that we have the following columns:
    # unit, sex, age, region, year, value
    df[['unit', 'sex', 'age', 'region']] = df['unit,sex,age,geo\\time'].str.split(',', expand=True)
    df.drop('unit,sex,age,geo\\time', axis=1, inplace=True)
    year_columns = df.columns.to_list()
    df_long = pd.melt(df,
                      id_vars=['unit', 'sex', 'age', 'region'],
                      value_vars=year_columns,
                      var_name='year',
                      value_name='value')

    # Ensures year is an int (with the appropriate data cleaning if required)
    df_long['year'] = df_long['year'].astype(int)

    # Ensures value is a float
    # (with the appropriate data cleaning if required, and do remove the NaNs)
    df_long['value'] = df_long['value'].astype(str).str.extract(r'([0-9,.]+)')
    df_long = df_long.dropna(subset=['value'])
    df_long['value'] = df_long['value'].astype(float)


    # Filters only the data where region equal to PT (Portugal).
    df_portugal = df_long[df_long['region'] == country]

    # Save the resulting data frame to the data folder as pt_life_expectancy.csv.
    # Ensure that no numerical index is saved.
    output_file_path = 'life_expectancy/data/pt_life_expectancy.csv'
    df_portugal.to_csv(output_file_path, index=False)

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description="Clean life expectancy data by country.")
    parser.add_argument('--country', type=str, default='PT', help='Country code (default: PT)')
    args = parser.parse_args()
    clean_data(args.country)
