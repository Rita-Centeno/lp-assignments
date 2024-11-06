import os
import argparse
import pandas as pd
from life_expectancy.cleaning import clean_data

current_dir = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(current_dir)
DATA_DIR = os.path.join(BASE_DIR, "data")
FIXTURES_DIR = os.path.join(BASE_DIR, "tests", "fixtures")

def create_fixture(country_code: str = 'PT') -> None:
    '''Creates a fixture to test'''

    original_data = pd.read_csv(DATA_DIR + '/eu_life_expectancy_raw.tsv', sep='\t')
    sample_data_in = original_data.sample(n=100, random_state=4)
    sample_data_in.to_csv(FIXTURES_DIR + 'eu_life_expectancy_raw_sample.tsv', index=False)

    sample_data_out = clean_data(sample_data_in, country_code)
    sample_data_out.to_csv(FIXTURES_DIR
                           + 'eu_life_expectancy_raw_sample_expected.csv',
                           index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--country', type=str, default='PT',
                        help='Country code to filter data (default: PT)')
    args = parser.parse_args()
    create_fixture(args.country)
