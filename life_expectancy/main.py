import os
import argparse
from life_expectancy.regions import Region
from life_expectancy.strategy import get_strategy

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, 'data')


def main(filter_country: Region = Region.PT) -> None:
    '''Main function to load, clean and save the data'''
    # Define the data paths
    #input_path = os.path.join(DATA_PATH, 'eu_life_expectancy_raw.tsv') # uncomment for tsv
    input_path = os.path.join(DATA_PATH, 'eurostat_life_expect.json') # uncomment for json
    output_file_name = f'{filter_country.name.lower()}_life_expectancy.csv'
    output_path = os.path.join(DATA_PATH, output_file_name)

    strategy = get_strategy(input_path)

    # Load, clean and save the data
    loaded_data = strategy.load_data_strategy(path=input_path)
    cleaned_data = strategy.clean_data_strategy(data=loaded_data, country=filter_country)
    strategy.save_data_strategy(data=cleaned_data, path=output_path)


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument('--country', type=lambda x: Region[x], default=Region.UK,
                    help='Country code (default: PT)')
    args = parser.parse_args()
    main(args.country)
