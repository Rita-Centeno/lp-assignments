import os
import argparse
import pandas as pd
from life_expectancy.cleaning import clean_data, clean_data_json
from life_expectancy.regions import Region

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")
FIXTURES_DIR = os.path.join(BASE_DIR, "tests\\fixtures\\")

def create_fixture(country_code: Region = Region.PT) -> None:
    '''Creates a fixture to test TSV-based data'''
    original_data = pd.read_csv(DATA_DIR + '/eu_life_expectancy_raw.tsv', sep='\t')

    sample_data_in = original_data.sample(n=1600, random_state=4)
    sample_data_in.to_csv(FIXTURES_DIR + 'eu_life_expectancy_raw_sample.tsv',
                           sep='\t', index=False)

    sample_data_out = clean_data(sample_data_in, country_code)
    sample_data_out.to_csv(FIXTURES_DIR
                           + 'eu_life_expectancy_raw_sample_expected.csv', index=False)

def create_fixture_json(country_code: Region = Region.PT) -> None:
    '''Creates a fixture to test JSON-based data'''
    original_data = pd.read_json(DATA_DIR + '/eurostat_life_expect.json')

    sample_data_in = original_data.sample(n=1600, random_state=4)
    sample_data_in.to_json(FIXTURES_DIR + 'eurostat_life_expect_sample.json',
                           orient='records', lines=False)

    sample_data_out = clean_data_json(sample_data_in, country_code)
    sample_data_out.to_csv(FIXTURES_DIR + 'eurostat_life_expect_sample_expected.csv', index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--country', type=lambda x: Region[x], default=Region.PT,
                    help='Country code (default: PT)')
    args = parser.parse_args()
    create_fixture(args.country)
    create_fixture_json(args.country)
